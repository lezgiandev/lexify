import { defineStore } from "pinia";
import {ref} from "vue";
import type { CompletedBook, Sentence } from "@/types";
import {
  addToCompletedBooks, deleteAllCompleted,
  getCompletedBooks,
  removeFromCompletedBooks,
} from "@/services/completedBookService.ts";


export const useCompletedBookStore = defineStore('completedBook', () => {
  const completedBooks = ref<CompletedBook[]>([]);
  const currentBookSentences = ref<Sentence[]>([]);
  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const fetchCompleted = async () => {
    isLoading.value = true;
    error.value = null;
    try {
      completedBooks.value = await getCompletedBooks();
    } catch (err) {
      error.value = 'Ошибка при загрузке прочитанных';
      console.error('Ошибка при загрузке прочитанных:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const addCompleted = async (bookId: number) => {
    try {
      if (isCompleted(bookId)) {
        console.warn('Книга уже в прочитанном');
        return;
      }

      await addToCompletedBooks(bookId);
      await fetchCompleted();
    } catch (err) {
      console.error('Ошибка при добавлении в избранное:', err);
      throw err;
    }
  };

  const removeCompleted = async (bookId: number) => {
    try {
      if (!isCompleted(bookId)) {
        console.warn('Книги нет в прочитанном!');
        return;
      }

      await removeFromCompletedBooks(bookId);
      await fetchCompleted();
    } catch (err) {
      console.error('Ошибка при удалении из прочитанного:', err);
      throw err;
    }
  };

  const removeAllCompleted = async () => {
    try {
      isLoading.value = true;
      await deleteAllCompleted();
      await fetchCompleted();
    } catch (err) {
      error.value = 'Ошибка при удалении всех прочитанных книг';
      console.error('Ошибка:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const isCompleted = (bookId: number) => {
    return completedBooks.value.some(cb => cb.book.id === bookId);
  };

  return {
    completedBooks,
    currentBookSentences,
    isLoading,
    error,
    removeAllCompleted,
    fetchCompleted,
    addCompleted,
    removeCompleted,
    isCompleted,
  };
});
