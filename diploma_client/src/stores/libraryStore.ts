import { defineStore } from 'pinia';
import { ref } from 'vue';
import {
  getBooks,
  getBookSentences,
} from '@/services/libraryService';
import type { Book, Sentence } from '@/types/types.ts';


export const useLibraryStore = defineStore('library', () => {

  const books = ref<Book[]>([]);
  const currentBookSentences = ref<Sentence[]>([]);
  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const currentPage = ref(1);
  const pageSize = ref(10);
  const totalCount = ref(0);

  const fetchBooks = async () => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await getBooks({
        page: currentPage.value,
      });
      books.value = response.results;
      totalCount.value = response.count;
    } catch (err) {
      error.value = 'Ошибка при загрузке книг';
      console.error('Ошибка при загрузке книг:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const fetchBookSentences = async (bookId: number) => {
    isLoading.value = true;
    try {
      currentBookSentences.value = await getBookSentences(bookId, {});

      if (!books.value.some(b => b.id === bookId)) {
        await fetchBooks();
      }
    } catch (err) {
      console.error('Ошибка при загрузке предложений:', err);
    } finally {
      isLoading.value = false;
    }
  };

  return {
    books,
    currentBookSentences,
    isLoading,
    error,
    currentPage,
    pageSize,
    totalCount,
    fetchBooks,
    fetchBookSentences,
  };
});
