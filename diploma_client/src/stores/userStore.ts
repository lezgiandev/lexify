import { getAllLanguages, getUserLanguage, updateUserLanguage } from "@/services/userService";
import { defineStore } from "pinia";
import { ref } from "vue";
import type {Language} from "@/types/types.ts";

export const useUserStore = defineStore('user', () => {
  const language = ref<Language | null>(null);
  const languages = ref<Language[]>([]);

  const fetchUserLanguage = async () => {
    try {
      language.value = await getUserLanguage();
    } catch (err) {
      console.error('Ошибка при загрузке языка:', err);
    }
  };

  const fetchAllLanguages = async () => {
    try {
      languages.value = await getAllLanguages();
    } catch (err) {
      console.error('Ошибка при загрузке языков:', err);
    }
  };

  const updateLanguage = async (languageId: number) => {
    try {
      await updateUserLanguage(languageId);
      await fetchUserLanguage();
    } catch (err) {
      console.error('Ошибка при изменении языка:', err);
      throw err;
    }
  };

  return {
    language,
    languages,
    fetchUserLanguage,
    fetchAllLanguages,
    updateLanguage,
  };
});
