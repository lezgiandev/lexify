<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useDictionaryStore } from '@/stores/dictionaryStore';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import { useFavoriteWordStore } from "@/stores/favoriteWordStore.ts";
import CustomListbox from "@/components/CustomListbox.vue";
import PaginationControls from "@/components/PaginationControls.vue";
import EmptyState from "@/components/EmptyState.vue";
import WordCard from "@/components/WordCard.vue";
import TrainingButton from "@/components/TrainingButton.vue";
import SearchInput from "@/components/SearchInput.vue";
import { useUserStore } from "@/stores/userStore.ts";

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
    dictionaryStore.currentPage = 1;
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

onMounted(async () => {
  await userStore.fetchUserLanguage();
  await dictionaryStore.fetchWords({});
  await dictionaryStore.fetchCategories();
  await dictionaryStore.fetchPartsOfSpeech();
  await favoriteWordStore.fetchFavorites();
});
</script>

<template>
  <div class="min-h-screen flex flex-col bg-zinc-900">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <div class="mb-8 relative">
        <h1 class="text-slate-100 text-3xl font-bold font-main">
          Словарь для языка: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-24 h-1 bg-violet-500 mt-2"></span>
        </h1>
        <p class="text-violet-500 text-lg mt-2 font-main font-semibold">
          Изменить язык можно в <router-link to="/settings" class="text-violet-500 hover:underline">настройках</router-link>
        </p>
      </div>

      <div class="mb-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 font-main">
        <SearchInput
          v-model="searchQuery"
          @update:modelValue="handleSearch"
        />

        <CustomListbox
          v-model="selectedCategory"
          :options="dictionaryStore.categories"
          defaultLabel="Все категории"
          @update:modelValue="handleFilterChange"
        />

        <CustomListbox
          v-model="selectedPartOfSpeech"
          :options="dictionaryStore.partsOfSpeech"
          defaultLabel="Все части речи"
          @update:modelValue="handleFilterChange"
        />

        <TrainingButton />
      </div>

      <div v-if="dictionaryStore.words.length > 0" class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-4 gap-4">
        <WordCard
          v-for="word in dictionaryStore.words"
          :key="word.id"
          :word="word.text"
          :wordId="word.id"
        />
      </div>

      <EmptyState v-else>
        Ничего не обнаружено
      </EmptyState>

      <PaginationControls
        v-if="totalPages > 1"
        :current-page="dictionaryStore.currentPage"
        :total-pages="totalPages"
        @prev="prevPage"
        @next="nextPage"
      />
    </main>
    <Footer />
  </div>
</template>
