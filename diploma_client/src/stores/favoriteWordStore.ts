import {defineStore} from "pinia";
import {ref} from "vue";
import type {FavoriteWord} from "@/types/types.ts";
import {
  addToFavorites,
  getFavoriteWords,
  removeFromFavorites
} from "@/services/favoriteWordService.ts";


export const useFavoriteWordStore = defineStore('favoriteWord', () => {
  const favorites = ref<FavoriteWord[]>([]);
  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const fetchFavorites = async () => {
    isLoading.value = true;
    error.value = null;
    try {
      favorites.value = await getFavoriteWords();
    } catch (err) {
      error.value = 'Ошибка при загрузке слов';
      console.error('Ошибка при загрузке слов:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const addFavorite = async (translationId: number) => {
    try {
      if (isFavorite(translationId)) {
        console.warn('Слово уже в избранном');
        return;
      }

      await addToFavorites(translationId);
      await fetchFavorites();
    } catch (err) {
      console.error('Ошибка при добавлении в избранное:', err);
      throw err;
    }
  };

  const removeFavorite = async (translationId: number) => {
    try {
      await removeFromFavorites(translationId);
      await fetchFavorites();
    } catch (err) {
      console.error('Ошибка при удалении из избранного:', err);
      throw err;
    }
  };

  const isFavorite = (translationId: number) => {
    return favorites.value.some((fav) => fav.translation.id === translationId);
  };

  return {
    favorites,
    isLoading,
    error,
    addFavorite,
    removeFavorite,
    fetchFavorites,
    isFavorite,
  };
});
