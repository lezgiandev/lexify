<script setup lang="ts">
import NavBar from "@/components/NavBar.vue";
import { useDictionaryStore } from '@/stores/dictionaryStore';
import { useUserStore } from "@/stores/userStore.ts";
import Footer from "@/components/Footer.vue";
import { onMounted } from "vue";
import { useFavoriteWordStore } from "@/stores/favoriteWordStore.ts";
import { useAuthStore } from '@/stores/authStore';

const authStore = useAuthStore();
const favoriteWordStore = useFavoriteWordStore();
const dictionaryStore = useDictionaryStore();
const userStore = useUserStore();

const playAudio = (audioUrl: string) => {
  if (audioUrl) {
    const audio = new Audio(audioUrl);
    audio.play();
  }
};

const isFavorite = (translationId: number) => {
  return favoriteWordStore.isFavorite(translationId);
};

const removeFromFavorites = async (translationId: number) => {
  await favoriteWordStore.removeFavorite(translationId);
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
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">

      <div class="mb-6">
        <h1 class="text-font-main text-xl md:text-2xl font-normal font-main">
          Словарь для языка: {{ userStore.language?.name }}
        </h1>
        <h2 class="text-font-colored text-xs md:text-sm font-normal font-main">
          Изменить язык словаря можно в разделе "Профиль"
        </h2>
      </div>

      <button
        @click="authStore.logout"
        class="text-xl font-main px-4 py-2 bg-button-cancel text-button-text font-semibold rounded-lg hover:bg-button-cancelhover transition duration-300"
        v-if="authStore.isAuthenticated"
      >Выйти</button>

      <div class="grid grid-cols-1 xl:grid-cols-2 2xl:grid-cols-2 gap-4">
        <div
          v-for="favoriteWord in favoriteWordStore.favorites"
          :key="favoriteWord.id"
          class="p-6 bg-background-two rounded-lg shadow-lg flex flex-col md:flex-row justify-between items-center"
        >

          <div class="flex flex-grow space-x-4 w-full md:w-auto font-main">
            <div class="flex-1 p-2 rounded-lg bg-background-three text-font-main text-center truncate font-semibold">
              {{ favoriteWord.translation.word.text }}
            </div>
            <div class="text-font-main self-center">
              —
            </div>
            <div class="flex-1 p-2 rounded-lg bg-background-three text-font-main text-center truncate font-semibold">
              {{ favoriteWord.translation.text }}
            </div>
          </div>

          <div class="flex space-x-4 mt-4 md:mt-0 md:ml-4 font-main">

            <button
              @click="playAudio(favoriteWord.translation.audio)"
              class="p-2 bg-button-main text-button-text rounded-lg hover:bg-button-mainhover transition duration-300"
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
              class="p-2 bg-button-cancel text-button-text rounded-lg hover:bg-button-cancelhover transition duration-300"
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
    </main>
    <Footer />
  </div>
</template>
