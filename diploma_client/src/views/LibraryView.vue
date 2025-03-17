<script setup lang="ts">
import { useLibraryStore } from '@/stores/libraryStore';
import { computed, onMounted } from 'vue';
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import { useUserStore } from "@/stores/userStore.ts";
import { useCompletedBookStore } from "@/stores/completedBookStore.ts";

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

// Исправленная функция проверки
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
          Изменить язык можно в <router-link to="/profile" class="text-button-main hover:underline">профиле</router-link>
        </p>
      </div>

      <div v-if="libraryStore.books.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div
          v-for="book in libraryStore.books"
          :key="book.id"
          class="p-4 bg-background-two rounded-xl"
        >
          <img :src="book.logo" class="w-full h-48 object-cover mb-4 rounded-xl"  alt=""/>
          <h3 class="text-2xl font-bold text-font-colored font-main mb-2">{{ book.title }}</h3>
          <p class="text-font-main text-lg font-main mb-4">{{ book.author }}</p>

          <div class="mt-4 flex justify-between items-center gap-4 font-main">
            <button
              @click="$router.push({ name: 'book', params: { bookId: book.id } })"
              class="flex-1 py-2 px-6 bg-button-main text-button-text rounded-xl font-semibold hover:bg-button-mainhover shadow-lg transition-all"
            >
              Читать
            </button>

            <button
              v-if="isCompleted(book.id)"
              @click="removeFromCompleted(book.id)"
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
              @click="addToCompleted(book.id)"
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
                  d="M5 13l4 4L19 7"
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
            Библиотека для выбранного языка пока недоступна
          </p>
        </div>
      </div>

      <!-- Пагинация -->
      <div class="mt-8 flex justify-center gap-4 font-main" v-if="totalPages > 1">
        <button
          @click="prevPage"
          :disabled="libraryStore.currentPage === 1"
          class="px-6 py-3 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300"
          :class="libraryStore.currentPage === 1
            ? 'bg-background-three text-font-main opacity-50 cursor-not-allowed'
            : 'bg-button-main text-button-text hover:bg-button-mainhover'"
        >
          ← Назад
        </button>

        <div class="flex items-center bg-background-two rounded-xl px-6 shadow-lg">
          <span class="text-font-main">
            Страница {{ libraryStore.currentPage }} <span class="opacity-50">из {{ totalPages }}</span>
          </span>
        </div>

        <button
          @click="nextPage"
          :disabled="libraryStore.currentPage >= totalPages"
          class="px-6 py-3 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300"
          :class="libraryStore.currentPage >= totalPages
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
