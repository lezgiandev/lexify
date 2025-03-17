import { defineStore } from "pinia";
import { ref } from "vue";
import type { MarkedSource } from "@/types/types.ts";
import {
  addToMarkedSources,
  getMarkedSources,
  removeFromMarkedSources
} from "@/services/markedSourceService.ts";

export const useMarkedSourceStore = defineStore('markedSource', () => {
  const markedSources = ref<MarkedSource[]>([]);
  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const fetchMarkedSources = async () => {
    isLoading.value = true;
    error.value = null;
    try {
      markedSources.value = await getMarkedSources();
    } catch (err) {
      error.value = 'Ошибка при загрузке отмеченных источников';
      console.error('Ошибка при загрузке отмеченных источников:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const addMarkedSource = async (sourceId: number) => {
    try {
      if (isMarked(sourceId)) {
        console.warn('Ссылка уже отмечена');
        return;
      }

      await addToMarkedSources(sourceId);
      await fetchMarkedSources();
    } catch (err) {
      console.error('Ошибка при добавлении отметки источника:', err);
      throw err;
    }
  };

  const removeMarkedSource = async (sourceId: number) => {
    try {
      await removeFromMarkedSources(sourceId);
      await fetchMarkedSources();
    } catch (err) {
      console.error('Ошибка при удалении отметки источника:', err);
      throw err;
    }
  };

  const isMarked = (sourceId: number) => {
    return markedSources.value.some((m) => m.source.id === sourceId);
  };

  return {
    markedSources,
    isLoading,
    error,
    addMarkedSource,
    removeMarkedSource,
    fetchMarkedSources,
    isMarked,
  };
});
