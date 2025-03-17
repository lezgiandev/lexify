import type { FavoriteWord } from "@/types/types.ts";
import axios from "axios";
import { API_URL } from "@/services/baseURL.ts";

export const getFavoriteWords = async (): Promise<FavoriteWord[]> => {
  try {
    const response = await axios.get<FavoriteWord[]>(`${API_URL}/favorite-words/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении избранных слов:', error);
    throw error;
  }
};

export const addToFavorites = async (translationId: number): Promise<void> => {
  try {
    await axios.post(
      `${API_URL}/favorite-words/`,
      { translation_id: translationId },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      }
    );
  } catch (error) {
    console.error('Ошибка при добавлении в избранное:', error);
    throw error;
  }
};

export const removeFromFavorites = async (translationId: number): Promise<void> => {
  try {
    await axios.delete(`${API_URL}/favorite-words/delete/`, {
      params: {
        translation_id: translationId,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
  } catch (error) {
    console.error('Ошибка при удалении из избранного:', error);
    throw error;
  }
};
