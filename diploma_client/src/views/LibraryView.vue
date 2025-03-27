<script setup lang="ts">
import { useLibraryStore } from '@/stores/libraryStore';
import {computed, onMounted, ref} from 'vue';
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import { useUserStore } from "@/stores/userStore.ts";
import { useCompletedBookStore } from "@/stores/completedBookStore.ts";
import PaginationControls from "@/components/PaginationControls.vue";
import EmptyState from "@/components/EmptyState.vue";
import BookCard from "@/components/BookCard.vue";
import SearchInput from "@/components/SearchInput.vue";
import CustomListbox from "@/components/CustomListbox.vue";

const completedBookStore = useCompletedBookStore();
const libraryStore = useLibraryStore();
const userStore = useUserStore();

const totalPages = computed(() => Math.ceil(libraryStore.totalCount / libraryStore.pageSize));

const searchQuery = ref('');
const selectedCategory = ref<number | null>(null);
const showOnlyMarked = ref(false);

const filteredBooks = computed(() => {
  if (!showOnlyMarked.value) return libraryStore.books;
  return libraryStore.books.filter(book =>
    completedBookStore.completedBooks.some(b => b.book.id === book.id)
  );
});

const toggleShowOnlyMarked = () => {
  showOnlyMarked.value = !showOnlyMarked.value;
};

const fetchBooks = async () => {
  await libraryStore.fetchBooks({
    category: selectedCategory.value ? Number(selectedCategory.value) : undefined,
    search: searchQuery.value,
  });
};

const handleFilterChange = () => {
  libraryStore.currentPage = 1;
  fetchBooks();
};

let searchTimeout: number | null = null;
const handleSearch = () => {
  if (searchTimeout) clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    libraryStore.currentPage = 1;
    fetchBooks();
  }, 300);
};

const addToCompleted = async (bookId: number) => {
  await completedBookStore.addCompleted(bookId);
};

const removeFromCompleted = async (bookId: number) => {
  await completedBookStore.removeCompleted(bookId);
};

const handleRemoveAll = async () => {
  if (confirm('Вы уверены, что хотите удалить все книги из прочитанного?')) {
    try {
      await completedBookStore.removeAllCompleted();
    } catch (err) {
      alert('Ошибка при удалении прочитанных книг');
    }
  }
};

const isCompleted = (bookId: number) => {
  return completedBookStore.completedBooks.some(cb => cb.book.id === bookId);
};

const nextPage = () => {
  libraryStore.currentPage += 1;
  fetchBooks();
};

const prevPage = () => {
  if (libraryStore.currentPage > 1) {
    libraryStore.currentPage -= 1;
    fetchBooks();
  }
};

onMounted(async () => {
  await userStore.fetchUserLanguage();
  await libraryStore.fetchBooks({});
  await libraryStore.fetchCategories();
  await completedBookStore.fetchCompleted();
});
</script>


<template>
  <div class="min-h-screen flex flex-col bg-zinc-900">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">

      <div class="mb-8 relative">
        <h1 class="text-font-main text-3xl font-bold font-main">
          Библиотека для языка: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-32 h-1 bg-violet-500 mt-2"></span>
        </h1>
        <p class="text-violet-500 text-lg mt-2 font-main">
          Изменить язык можно в <router-link to="/settings" class="text-violet-500 hover:underline">настройках</router-link>
        </p>
      </div>

      <div class="mb-8 grid grid-cols-1 md:grid-cols-4 gap-4 font-main">
        <SearchInput
          v-model="searchQuery"
          @update:modelValue="handleSearch"
        />

        <CustomListbox
          v-model="selectedCategory"
          :options="libraryStore.categories"
          defaultLabel="Все категории"
          @update:modelValue="handleFilterChange"
        />

        <button
          @click="toggleShowOnlyMarked"
          class="p-4 bg-violet-500 text-white rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-violet-700 transition-all duration-300 flex items-center justify-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
          {{ showOnlyMarked ? 'Показать все' : 'Только отмеченные' }}
        </button>

        <button
          @click="handleRemoveAll"
          class="p-4 bg-button-cancel text-white rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-button-cancelhover transition-all duration-300 flex items-center justify-center gap-2"
          :disabled="completedBookStore.isLoading"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
          </svg>
          Удалить пометки
        </button>
      </div>

      <div v-if="filteredBooks.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <BookCard
          v-for="book in filteredBooks"
          :key="book.id"
          :title="book.title"
          :logo="book.logo"
          :author="book.author"
          :is-completed="isCompleted(book.id)"
          :bookId="book.id"
          @add-to-completed="addToCompleted"
          @remove-from-completed="removeFromCompleted"
        />
      </div>

      <EmptyState v-else>
        Библиотека для выбранного языка пока недоступна
      </EmptyState>

      <PaginationControls
        v-if="totalPages > 1"
        :current-page="libraryStore.currentPage"
        :total-pages="totalPages"
        @prev="prevPage"
        @next="nextPage"
      />
    </main>
    <Footer />
  </div>
</template>
