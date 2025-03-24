<script setup lang="ts">
import { useLibraryStore } from '@/stores/libraryStore';
import { computed, onMounted } from 'vue';
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import { useUserStore } from "@/stores/userStore.ts";
import { useCompletedBookStore } from "@/stores/completedBookStore.ts";
import PaginationControls from "@/components/PaginationControls.vue";
import EmptyState from "@/components/EmptyState.vue";
import BookCard from "@/components/BookCard.vue";

const completedBookStore = useCompletedBookStore();
const libraryStore = useLibraryStore();
const userStore = useUserStore();

const totalPages = computed(() => Math.ceil(libraryStore.totalCount / libraryStore.pageSize));

const fetchBooks = async () => {
  await libraryStore.fetchBooks();
};

const addToCompleted = async (bookId: number) => {
  await completedBookStore.addCompleted(bookId);
};

const removeFromCompleted = async (bookId: number) => {
  await completedBookStore.removeCompleted(bookId);
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
  await libraryStore.fetchBooks();
  await completedBookStore.fetchCompleted();
});
</script>


<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">

      <div class="mb-8 relative">
        <h1 class="text-font-main text-3xl font-bold font-great">
          Библиотека для языка: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-32 h-1 bg-button-main mt-2"></span>
        </h1>
        <p class="text-font-colored text-lg mt-2 font-main">
          Изменить язык можно в <router-link to="/settings" class="text-button-main hover:underline">настройках</router-link>
        </p>
      </div>

      <div v-if="libraryStore.books.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <BookCard
          v-for="book in libraryStore.books"
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
