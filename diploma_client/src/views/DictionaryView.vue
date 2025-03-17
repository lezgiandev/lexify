<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useDictionaryStore } from '@/stores/dictionaryStore';
import { Listbox, ListboxButton, ListboxOptions, ListboxOption } from '@headlessui/vue'
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import { useUserStore } from "@/stores/userStore.ts";
import { useFavoriteWordStore } from "@/stores/favoriteWordStore.ts";

const favoriteWordStore = useFavoriteWordStore();
const dictionaryStore = useDictionaryStore();
const userStore = useUserStore();

const searchQuery = ref('');
const selectedCategory = ref<number | null>(null);
const selectedPartOfSpeech = ref<number | null>(null);

const totalPages = computed(() => Math.ceil(dictionaryStore.totalCount / dictionaryStore.pageSize));

const fetchWords = async () => {
  await dictionaryStore.fetchWords({
    category: selectedCategory.value ? Number(selectedCategory.value) : undefined,
    partOfSpeech: selectedPartOfSpeech.value ? Number(selectedPartOfSpeech.value) : undefined,
    search: searchQuery.value,
  });
};

const handleFilterChange = () => {
  dictionaryStore.currentPage = 1;
  fetchWords();
};

let searchTimeout: number | null = null;
const handleSearch = () => {
  if (searchTimeout) clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    dictionaryStore.currentPage = 1; // Сброс страницы
    fetchWords();
  }, 300);
};

const nextPage = () => {
  dictionaryStore.currentPage += 1;
  fetchWords();
};

const prevPage = () => {
  if (dictionaryStore.currentPage > 1) {
    dictionaryStore.currentPage -= 1;
    fetchWords();
  }
};

const playAudio = (audioUrl: string) => {
  if (audioUrl) {
    const audio = new Audio(audioUrl);
    audio.play();
  }
};

const addToFavorites = async (translationId: number) => {
  await favoriteWordStore.addFavorite(translationId);
};

const removeFromFavorites = async (translationId: number) => {
  await favoriteWordStore.removeFavorite(translationId);
};

const isFavorite = (translationId: number) => {
  return favoriteWordStore.isFavorite(translationId);
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
      <!-- Заголовок с акцентной линией -->
      <div class="mb-8 relative">
        <h1 class="text-font-main text-3xl font-bold font-great">
          Словарь: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-24 h-1 bg-button-main mt-2"></span>
        </h1>
        <p class="text-font-colored text-lg mt-2 font-main">
          Изменить язык можно в <router-link to="/profile" class="text-button-main hover:underline">профиле</router-link>
        </p>
      </div>

      <!-- Фильтры с современным дизайном -->
      <div class="mb-8 grid grid-cols-1 md:grid-cols-4 gap-4 font-main">
        <!-- Поиск -->
        <div class="relative group">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Поиск..."
            class="w-full p-4 bg-background-two text-font-main rounded-xl focus:outline-none focus:ring-2 focus:ring-button-main shadow-lg hover:shadow-xl transition-all duration-300 pr-12"
            @input="handleSearch"
          />
          <svg class="w-5 h-5 absolute right-4 top-4 text-button-main opacity-70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
        </div>

        <!-- Выпадающие списки -->
        <Listbox v-model="selectedCategory" @update:modelValue="handleFilterChange">
          <div class="relative group">
            <ListboxButton class="w-full p-4 bg-background-two text-font-main rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 text-left pr-12">
              {{ dictionaryStore.categories.find(c => c.id === selectedCategory)?.name || 'Все категории' }}
              <span class="absolute inset-y-0 right-4 flex items-center">
                <svg class="w-5 h-5 text-button-main transform group-hover:rotate-180 transition duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                </svg>
              </span>
            </ListboxButton>

            <ListboxOptions class="absolute z-20 w-full mt-2 bg-background-two rounded-xl shadow-2xl overflow-hidden">
              <ListboxOption
                :value="null"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-two text-font-main',
                    'p-3 transition-colors'
                  ]"
                >
                  Все категории
                </li>
              </ListboxOption>

              <ListboxOption
                v-for="category in dictionaryStore.categories"
                :key="category.id"
                :value="category.id"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-two text-font-main',
                    'p-3 transition-colors'
                  ]"
                >
                  {{ category.name }}
                </li>
              </ListboxOption>
            </ListboxOptions>
          </div>
        </Listbox>

        <Listbox v-model="selectedPartOfSpeech" @update:modelValue="handleFilterChange">
          <div class="relative group">
            <ListboxButton
              class="w-full p-4 bg-background-two text-font-main rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 text-left pr-12"
            >
              {{ dictionaryStore.partsOfSpeech.find(p => p.id === selectedPartOfSpeech)?.name || 'Все части речи' }}

              <span class="absolute inset-y-0 right-4 flex items-center">
                <svg class="w-5 h-5 text-button-main transform group-hover:rotate-180 transition duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                </svg>
              </span>
            </ListboxButton>

            <ListboxOptions class="absolute z-20 w-full mt-2 bg-background-two rounded-xl shadow-2xl overflow-hidden">
              <ListboxOption
                :value="null"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-two text-font-main',
                    'p-3 transition-colors'
                  ]"
                >
                  Все части речи
                </li>
              </ListboxOption>

              <ListboxOption
                v-for="part in dictionaryStore.partsOfSpeech"
                :key="part.id"
                :value="part.id"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-two text-font-main',
                    'p-3 transition-colors'
                  ]"
                >
                  {{ part.name }}
                </li>
              </ListboxOption>
            </ListboxOptions>
          </div>
        </Listbox>

        <button class="p-4 bg-button-main text-button-text rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-button-mainhover transition-all duration-300 flex items-center justify-center gap-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
          Заучивание
        </button>
      </div>

      <div v-if="dictionaryStore.translations.length > 0" class="grid grid-cols-1 xl:grid-cols-2 2xl:grid-cols-2 gap-4">
        <div
          v-for="translation in dictionaryStore.translations"
          :key="translation.id"
          class="p-6 bg-background-two rounded-2xl shadow-lg flex flex-col md:flex-row justify-between items-center"
        >
          <div class="flex flex-grow space-x-4 w-full md:w-auto font-main">
            <div class="flex-1 p-2 rounded-lg bg-background-three text-font-main text-center truncate font-semibold">
              {{ translation.word.text }}
            </div>
            <div class="text-font-main self-center text-2xl">
              →
            </div>
            <div class="flex-1 p-2 rounded-lg bg-background-three text-font-main text-center truncate font-semibold">
              {{ translation.text }}
            </div>
          </div>

          <div class="flex space-x-4 mt-4 md:mt-0 md:ml-4 font-main">
            <button
              @click="playAudio(translation.audio)"
              class="p-2 bg-button-main/20 text-button-main rounded-xl hover:bg-button-main hover:text-button-text transition duration-300"
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
              v-if="isFavorite(translation.id)"
              @click="removeFromFavorites(translation.id)"
              class="p-2 rounded-xl transition duration-300 bg-button-cancel/20 text-button-cancel hover:bg-button-cancel hover:text-button-text"
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

            <button
              v-else
              @click="addToFavorites(translation.id)"
              class="p-2 rounded-xl transition duration-300 bg-button-main/20 text-button-main hover:bg-button-main hover:text-button-text"
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
                  d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Пустое состояние -->
      <div v-else class="text-center py-12">
        <div class="inline-flex flex-col items-center max-w-md mx-auto animate-fade-in">
          <div class="relative mb-6">
            <div class="w-32 h-32 bg-button-main/10 rounded-full animate-pulse"></div>
            <svg class="w-20 h-20 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-button-main"
                 fill="none"
                 stroke="currentColor"
                 viewBox="0 0 24 24">
              <path stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="1.5"
                    d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
            </svg>
          </div>
          <p class="text-font-main text-xl font-medium mb-4">
            Словарь для выбранного языка пока недоступен
          </p>
        </div>
      </div>

      <!-- Пагинация -->
      <div class="mt-8 flex justify-center gap-4 font-main" v-if="totalPages > 1">
        <button
          @click="prevPage"
          :disabled="dictionaryStore.currentPage === 1"
          class="px-6 py-3 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300"
          :class="dictionaryStore.currentPage === 1
            ? 'bg-background-three text-font-main opacity-50 cursor-not-allowed'
            : 'bg-button-main text-button-text hover:bg-button-mainhover'"
        >
          ← Назад
        </button>

        <div class="flex items-center bg-background-two rounded-xl px-6 shadow-lg">
          <span class="text-font-main">
            Страница {{ dictionaryStore.currentPage }} <span class="opacity-50">из {{ totalPages }}</span>
          </span>
        </div>

        <button
          @click="nextPage"
          :disabled="dictionaryStore.currentPage >= totalPages"
          class="px-6 py-3 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300"
          :class="dictionaryStore.currentPage >= totalPages
            ? 'bg-background-three text-font-main opacity-50 cursor-not-allowed'
            : 'bg-button-main text-button-text hover:bg-button-mainhover'"
        >
          Вперед →
        </button>
      </div>
    </main>
    <Footer />
  </div>
</template>
