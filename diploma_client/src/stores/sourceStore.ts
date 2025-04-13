import {defineStore} from "pinia";
import {ref} from "vue";
import type {
  Source,
  SourceCategory,
} from "@/types";
import { getCategories, getSources } from "@/services/sourceService.ts";

export const useSourceStore = defineStore('source', () => {
  const sources = ref<Source[]>([]);
  const categories = ref<SourceCategory[]>([]);

  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const currentPage = ref(1);
  const pageSize = ref(20);
  const totalCount = ref(0);

  const fetchSources = async (params: {
    category?: number;
    search?: string;
  }) => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await getSources({
        ...params,
        page: currentPage.value,
      });
      sources.value = response.results;
      totalCount.value = response.count;
    } catch (err) {
      error.value = 'Ошибка при загрузке источников';
      console.error('Ошибка при загрузке источников:', err);
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

  return {
    sources,
    isLoading,
    error,
    currentPage,
    pageSize,
    totalCount,
    categories,
    fetchSources,
    fetchCategories,
  };
});
