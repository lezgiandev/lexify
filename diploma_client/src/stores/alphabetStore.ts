import { defineStore } from "pinia";
import { ref } from "vue";
import type { Letter } from "@/types";
import {getLetters} from "@/services/alphabetService.ts";

export const useAlphabetStore = defineStore('alphabet', () => {
  const letters = ref<Letter[]>([])

  const fetchAllLetters = async () => {
    try {
      letters.value = await getLetters();
    } catch (err) {
      console.error('Ошибка при загрузке букав:', err);
    }
  };

  return {
    letters,
    fetchAllLetters,
  }
});
