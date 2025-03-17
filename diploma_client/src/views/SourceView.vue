<script setup lang="ts">
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import { useUserStore } from "@/stores/userStore";
import { useSourceStore } from "@/stores/sourceStore";
import { useMarkedSourceStore } from "@/stores/markedSourceStore";
import {computed, onMounted, ref} from "vue";
import {Listbox, ListboxButton, ListboxOption, ListboxOptions} from "@headlessui/vue";

const userStore = useUserStore();
const sourceStore = useSourceStore();
const markedSourceStore = useMarkedSourceStore();

const searchQuery = ref('');
const selectedCategory = ref<number | null>(null);

const totalPages = computed(() => Math.ceil(sourceStore.totalCount / sourceStore.pageSize));

const fetchSources = async () => {
  await sourceStore.fetchSources({
    category: selectedCategory.value ? Number(selectedCategory.value) : undefined,
    search: searchQuery.value,
  });
};

const handleFilterChange = () => {
  sourceStore.currentPage = 1;
  fetchSources();
};

let searchTimeout: number | null = null;
const handleSearch = () => {
  if (searchTimeout) clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    sourceStore.currentPage = 1;
    fetchSources();
  }, 300);
};

const nextPage = () => {
  sourceStore.currentPage += 1;
  fetchSources();
};

const prevPage = () => {
  if (sourceStore.currentPage > 1) {
    sourceStore.currentPage -= 1;
    fetchSources();
  }
};

const addToMarked = async (sourceId: number) => {
  await markedSourceStore.addMarkedSource(sourceId);
};

const removeFromMarked= async (sourceId: number) => {
  await markedSourceStore.removeMarkedSource(sourceId);
};

const isMarked = (sourceId: number) => {
  return markedSourceStore.isMarked(sourceId);
};

onMounted(async () => {
  await userStore.fetchUserLanguage();
  await sourceStore.fetchSources({});
  await sourceStore.fetchCategories();
});
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <!-- Заголовок с акцентной линией -->
      <div class="mb-8 relative">
        <h1 class="text-font-main text-3xl font-bold font-great">
          Источники: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-48 h-1 bg-button-main mt-2"></span>
        </h1>
        <p class="text-font-colored text-lg mt-2 font-main">
          Изменить язык можно в <router-link to="/profile" class="text-button-main hover:underline">профиле</router-link>
        </p>
      </div>

      <!-- Фильтры -->
      <div class="mb-8 grid grid-cols-1 md:grid-cols-2 gap-4 font-main">
        <div class="relative group">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Поиск источников..."
            class="w-full p-4 bg-background-two text-font-main rounded-xl focus:outline-none focus:ring-2 focus:ring-button-main shadow-lg hover:shadow-xl transition-all duration-300 pr-12"
            @input="handleSearch"
          />
          <svg class="w-5 h-5 absolute right-4 top-4 text-button-main opacity-70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
        </div>

        <Listbox v-model="selectedCategory" @update:modelValue="handleFilterChange">
          <div class="relative group">
            <ListboxButton class="w-full p-4 bg-background-two text-font-main rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 text-left pr-12">
              {{ sourceStore.categories.find(c => c.id === selectedCategory)?.name || 'Все категории' }}
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
                v-for="category in sourceStore.categories"
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
      </div>

      <div v-if="sourceStore.sources.length > 0" class="grid grid-cols-1 xl:grid-cols-2 2xl:grid-cols-2 gap-4">
        <div
          v-for="source in sourceStore.sources"
          :key="source.id"
          class="p-6 bg-background-two rounded-xl shadow-lg flex flex-col md:flex-row justify-between items-center"
        >
          <div class="flex flex-grow space-x-4 w-full md:w-auto font-main">
            <h3 class="text-font-main text-xl font-medium truncate">{{ source.text }}</h3>
          </div>

          <div class="flex space-x-4 mt-4 md:mt-0 md:ml-4 font-main">
            <a
              :href="source.link"
              target="_blank"
              class="px-6 py-2 bg-button-main text-button-text rounded-xl font-semibold hover:bg-button-mainhover shadow-lg hover:shadow-xl transition-all flex items-center gap-2"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
              </svg>
              Перейти
            </a>

            <button
              v-if="isMarked(source.id)"
              @click="removeFromMarked(source.id)"
              class="p-2 rounded-xl shadow-lg hover:shadow-xl transition-all bg-button-cancel/20 text-button-cancel hover:bg-button-cancel hover:text-button-text"
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
              @click="addToMarked(source.id)"
              class="p-2 rounded-xl shadow-lg hover:shadow-xl transition-all bg-button-main/20 text-button-main hover:bg-button-main hover:text-button-text"
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
                    d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/>
            </svg>
          </div>
          <p class="text-font-main text-xl font-medium mb-4">
            Источники для выбранного языка пока недоступны
          </p>
        </div>
      </div>

      <!-- Пагинация -->
      <div class="mt-8 flex justify-center gap-4 font-main" v-if="totalPages > 1">
        <button
          @click="prevPage"
          :disabled="sourceStore.currentPage === 1"
          class="px-6 py-3 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300"
          :class="sourceStore.currentPage === 1
            ? 'bg-background-three text-font-main opacity-50 cursor-not-allowed'
            : 'bg-button-main text-button-text hover:bg-button-mainhover'"
        >
          ← Назад
        </button>

        <div class="flex items-center bg-background-two rounded-xl px-6 shadow-lg">
          <span class="text-font-main">
            Страница {{ sourceStore.currentPage }} <span class="opacity-50">из {{ totalPages }}</span>
          </span>
        </div>

        <button
          @click="nextPage"
          :disabled="sourceStore.currentPage >= totalPages"
          class="px-6 py-3 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300"
          :class="sourceStore.currentPage >= totalPages
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

<style>
.animate-fade-in {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
