import { defineStore } from 'pinia';
import { ref } from 'vue';
import {
  getCategories,
  getPartsOfSpeech,
  getWords, getWordTranslations,
} from '@/services/dictionaryService';
import type {DictionaryCategory, PartOfSpeech, Translation, Word} from '@/types/types.ts';

export const useDictionaryStore = defineStore('dictionary', () => {
  const words = ref<Word[]>([]);
  const categories = ref<DictionaryCategory[]>([]);
  const partsOfSpeech = ref<PartOfSpeech[]>([])
  const currentWordTranslations = ref<Translation[]>([]);

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
      words.value = response.results;
      totalCount.value = response.count;
    } catch (err) {
      error.value = 'Ошибка при загрузке слов';
      console.error('Ошибка при загрузке слов:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const fetchWordTranslations = async (wordId: number) => {
    isLoading.value = true;
    try {
      currentWordTranslations.value = await getWordTranslations(wordId, {});

      if (!words.value.some(b => b.id === wordId)) {
        await fetchWords({});
      }
    } catch (err) {
      console.error('Ошибка при загрузке переводов:', err);
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
    words,
    isLoading,
    error,
    currentPage,
    pageSize,
    totalCount,
    categories,
    partsOfSpeech,
    currentWordTranslations,
    fetchWordTranslations,
    fetchWords,
    fetchCategories,
    fetchPartsOfSpeech,
  };
});
