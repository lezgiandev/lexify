<script setup lang="ts">
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import { useUserStore } from "@/stores/userStore";
import { useSourceStore } from "@/stores/sourceStore";
import { useMarkedSourceStore } from "@/stores/markedSourceStore";
import {computed, onMounted, ref} from "vue";
import PaginationControls from "@/components/PaginationControls.vue";
import EmptyState from "@/components/EmptyState.vue";
import CustomListbox from "@/components/CustomListbox.vue";
import SearchInput from "@/components/SearchInput.vue";
import SourceCard from "@/components/SourceCard.vue";

const userStore = useUserStore();
const sourceStore = useSourceStore();
const markedSourceStore = useMarkedSourceStore();

const searchQuery = ref('');
const selectedCategory = ref<number | null>(null);
const showOnlyMarked = ref(false);

const filteredSources = computed(() => {
  if (!showOnlyMarked.value) return sourceStore.sources;
  return sourceStore.sources.filter(source =>
    markedSourceStore.markedSources.some(m => m.source.id === source.id)
  );
});

const toggleShowOnlyMarked = () => {
  showOnlyMarked.value = !showOnlyMarked.value;
};

const totalPages = computed(() => {
  const total = showOnlyMarked.value
    ? filteredSources.value.length
    : sourceStore.totalCount;
  return Math.ceil(total / sourceStore.pageSize);
});

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

const handleRemoveAll = async () => {
  if (confirm('Вы уверены, что хотите удалить все источники из отмеченного?')) {
    try {
      await markedSourceStore.removeAllMarks();
    } catch (err) {
      alert('Ошибка при удалении источников');
    }
  }
};

const isMarked = (sourceId: number) => {
  return markedSourceStore.isMarked(sourceId);
};

onMounted(async () => {
  await userStore.fetchUserLanguage();
  await sourceStore.fetchSources({});
  await sourceStore.fetchCategories();
  await markedSourceStore.fetchMarkedSources();
});
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <div class="mb-8 relative">
        <h1 class="text-font-main text-3xl font-bold font-great">
          Источники: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-48 h-1 bg-button-main mt-2"></span>
        </h1>
        <p class="text-font-colored text-lg mt-2 font-main">
          Изменить язык можно в <router-link to="/settings" class="text-button-main hover:underline">настройках</router-link>
        </p>
      </div>

      <div class="mb-8 grid grid-cols-1 md:grid-cols-4 gap-4 font-main">
        <SearchInput
          v-model="searchQuery"
          @update:modelValue="handleSearch"
        />

        <CustomListbox
          v-model="selectedCategory"
          :options="sourceStore.categories"
          defaultLabel="Все категории"
          @update:modelValue="handleFilterChange"
        />

        <button
          @click="toggleShowOnlyMarked"
          class="p-4 bg-button-main text-button-text rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-button-mainhover transition-all duration-300 flex items-center justify-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
          {{ showOnlyMarked ? 'Показать все' : 'Только отмеченные' }}
        </button>

        <button
          @click="handleRemoveAll"
          class="p-4 bg-button-cancel text-button-text rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-button-cancelhover transition-all duration-300 flex items-center justify-center gap-2"
          :disabled="markedSourceStore.isLoading"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
          </svg>
          Удалить все
        </button>
      </div>

      <div v-if="filteredSources.length > 0" class="grid grid-cols-1 xl:grid-cols-1 2xl:grid-cols-2 gap-4">
        <SourceCard
          v-for="source in filteredSources"
          :key="source.id"
          :text="source.text"
          :link="source.link"
          :isMarked="isMarked(source.id)"
          :sourceId="source.id"
          @add-to-marked="addToMarked"
          @remove-from-marked="removeFromMarked"
        />
      </div>

      <EmptyState v-else>
        Источники для выбранного языка не найдены
      </EmptyState>

      <PaginationControls
        v-if="totalPages > 1"
        :current-page="sourceStore.currentPage"
        :total-pages="totalPages"
        @prev="prevPage"
        @next="nextPage"
      />
    </main>
    <Footer />
  </div>
</template>

<style>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
