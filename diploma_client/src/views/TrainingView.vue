<script setup lang="ts">
import NavBar from "@/components/NavBar.vue";
import { useDictionaryStore } from '@/stores/dictionaryStore';
import { useUserStore } from "@/stores/userStore.ts";
import Footer from "@/components/Footer.vue";
import { onMounted } from "vue";
import { useFavoriteWordStore } from "@/stores/favoriteWordStore.ts";
import { ref } from "vue";
import TrainingModal from "@/components/TrainingModal.vue";
import type {FavoriteWord} from "@/types/types.ts";
import EmptyState from "@/components/EmptyState.vue";

const favoriteWordStore = useFavoriteWordStore();
const dictionaryStore = useDictionaryStore();
const userStore = useUserStore();

const showTrainingModal = ref(false);
const shuffledWords = ref<FavoriteWord[]>([]);

const playAudio = (audioUrl: string) => {
  if (audioUrl) {
    const audio = new Audio(audioUrl);
    audio.play();
  }
};

const handleRemoveAll = async () => {
  if (confirm('Вы уверены, что хотите удалить все слова из избранного?')) {
    try {
      await favoriteWordStore.removeAllFavorites();
    } catch (err) {
      alert('Ошибка при удалении слов');
    }
  }
};

const isFavorite = (translationId: number) => {
  return favoriteWordStore.isFavorite(translationId);
};

const removeFromFavorites = async (translationId: number) => {
  await favoriteWordStore.removeFavorite(translationId);
};

const startTraining = () => {
  shuffledWords.value = [...favoriteWordStore.favorites].sort(() => Math.random() - 0.5);
  showTrainingModal.value = true;
};

onMounted(async () => {
  await userStore.fetchUserLanguage();
  await dictionaryStore.fetchWords({});
  await dictionaryStore.fetchCategories();
  await dictionaryStore.fetchPartsOfSpeech();
  await favoriteWordStore.fetchFavorites();
});
</script>

<template>
  <div class="min-h-screen flex flex-col bg-zinc-900">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <div class="mb-8 relative">
        <h1 class="text-white text-3xl font-bold font-main">
          Режим тренировки языка: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-36 h-1 bg-violet-500 mt-2"></span>
        </h1>
        <p class="text-violet-500 font-semibold text-lg mt-2 font-main">
          Изменить язык можно в <router-link to="/settings" class="text-violet-500 hover:underline">настройках</router-link>
        </p>
      </div>

      <div class="mb-8 grid grid-cols-1 md:grid-cols-4 gap-4 font-main">
        <router-link
          to="/dictionary"
          class="p-4 bg-violet-500 text-gray-100 rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-violet-700 transition-all duration-300 flex items-center justify-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
          </svg>
          Назад к словарю
        </router-link>

        <button
          @click="startTraining"
          :disabled="favoriteWordStore.favorites.length === 0"
          class="p-4 bg-violet-500 text-gray-100 rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-violet-700 transition-all duration-300 flex items-center justify-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
          Тренировка!
        </button>

        <button
          @click="handleRemoveAll"
          class="p-4 bg-button-cancel text-gray-100 rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-button-cancelhover transition-all duration-300 flex items-center justify-center gap-2"
          :disabled="favoriteWordStore.isLoading"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
          </svg>
          Удалить все
        </button>
      </div>

      <div
        v-if="favoriteWordStore.favorites.length > 0"
        class="grid grid-cols-1 xl:grid-cols-2 2xl:grid-cols-2 gap-4"
      >
        <div
          v-for="favoriteWord in favoriteWordStore.favorites"
          :key="favoriteWord.id"
          class="p-4 bg-zinc-800 rounded-2xl shadow-lg flex flex-col md:flex-row justify-between items-center"
        >
          <div class="flex flex-grow space-x-4 w-full md:w-auto font-main">
            <div class="flex-1 p-2 rounded-lg text-xl text-white text-center truncate font-bold">
              {{ favoriteWord.translation.word.text }}
            </div>
            <div class="text-white self-center text-2xl">
              →
            </div>
            <div class="flex-1 p-2 rounded-lg text-xl text-white text-center truncate font-bold">
              {{ favoriteWord.translation.text }}
            </div>
          </div>

          <div class="flex space-x-4 mt-4 md:mt-0 md:ml-4 font-main">
            <button
              @click="playAudio(favoriteWord.translation.audio)"
              class="p-2 bg-violet-500/20 text-violet-500 rounded-xl hover:bg-violet-500 hover:text-zinc-800 transition duration-300"
            >
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"
                />
              </svg>
            </button>

            <button
              v-if="isFavorite(favoriteWord.translation.id)"
              @click="removeFromFavorites(favoriteWord.translation.id)"
              class="p-2 rounded-xl transition duration-300 bg-button-cancel/20 text-button-cancel hover:bg-button-cancel hover:text-zinc-800"
            >
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <EmptyState v-else>
        У вас не добавлено в избранное ни одного слова
      </EmptyState>

      <TrainingModal
        v-if="showTrainingModal"
        :words="shuffledWords"
        @close="showTrainingModal = false"
      />
    </main>
    <Footer />
  </div>
</template>
