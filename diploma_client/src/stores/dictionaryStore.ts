import { defineStore } from 'pinia';
import { ref } from 'vue';
import {
  getCategories,
  getPartsOfSpeech,
  getWords,
} from '@/services/dictionaryService';
import type { DictionaryCategory, PartOfSpeech, Translation } from '@/types/types.ts';

export const useDictionaryStore = defineStore('dictionary', () => {
  const translations = ref<Translation[]>([]);
  const categories = ref<DictionaryCategory[]>([]);
  const partsOfSpeech = ref<PartOfSpeech[]>([])

  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const currentPage = ref(1);
  const pageSize = ref(20);
  const totalCount = ref(0);

  const fetchWords = async (params: {
    category?: number;
    partOfSpeech?: number;
    search?: string;
  }) => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await getWords({
        ...params,
        page: currentPage.value,
      });
      translations.value = response.results;
      totalCount.value = response.count;
    } catch (err) {
      error.value = 'Ошибка при загрузке слов';
      console.error('Ошибка при загрузке слов:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const fetchCategories = async () => {
    try {
      categories.value = await getCategories();
    } catch (err) {
      console.error('Ошибка при загрузке категорий:', err);
    }
  };

  const fetchPartsOfSpeech = async () => {
    try {
      partsOfSpeech.value = await getPartsOfSpeech();
    } catch (err) {
      console.error('Ошибка при загрузке частей речи:', err);
    }
  };

  return {
    translations,
    isLoading,
    error,
    currentPage,
    pageSize,
    totalCount,
    categories,
    partsOfSpeech,
    fetchWords,
    fetchCategories,
    fetchPartsOfSpeech,
  };
});
