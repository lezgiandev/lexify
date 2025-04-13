import axios from 'axios';
import { API_URL } from '@/services/baseURL';
import type {
  DictionaryCategory,
  DictionaryResponse,
  PartOfSpeech, Translation
} from '@/types';

export const getWords = async (params: {
  category?: number;
  partOfSpeech?: number;
  search?: string;
  page?: number;
}): Promise<DictionaryResponse> => {
  try {
    const response = await axios.get<DictionaryResponse>(`${API_URL}/dictionary/`, {
      params: {
        category: params.category,
        part_of_speech: params.partOfSpeech,
        search: params.search,
        page: params.page,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении слов:', error);
    throw error;
  }
};

export const getWordTranslations = async (wordId: number, params: {
  page?: number;
}): Promise<Translation[]> => {
  try {
    const response = await axios.get<Translation[]>(`${API_URL}/dictionary/${wordId}/translations/`, {
      params: {
        page: params.page,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении переводов:', error);
    throw error;
  }
};

export const getCategories = async (): Promise<DictionaryCategory[]> => {
  try {
    const response = await axios.get<DictionaryCategory[]>(`${API_URL}/dictionary-categories/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении категорий словаря:', error);
    throw error;
  }
};

export const getPartsOfSpeech = async (): Promise<PartOfSpeech[]> => {
  try {
    const response = await axios.get<PartOfSpeech[]>(`${API_URL}/parts-of-speech/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении частей речи:', error);
    throw error;
  }
};
