import type { CompletedBook } from "@/types";
import axios from "axios";
import { API_URL } from "@/services/baseURL.ts";

export const getCompletedBooks = async (): Promise<CompletedBook[]> => {
  try {
    const response = await axios.get<CompletedBook[]>(`${API_URL}/completed-books/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении прочитанных книг:', error);
    throw error;
  }
};

export const addToCompletedBooks = async (bookId: number): Promise<void> => {
  try {
    await axios.post(
      `${API_URL}/completed-books/`,
      { book_id: bookId },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      }
    );
  } catch (error) {
    console.error('Ошибка при добавлении в прочитанное:', error);
    throw error;
  }
};

export const removeFromCompletedBooks = async (bookId: number): Promise<void> => {
  try {
    await axios.delete(`${API_URL}/completed-books/delete/`, {
      params: {
        book_id: bookId,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
  } catch (error) {
    console.error('Ошибка при удалении из прочитанного:', error);
    throw error;
  }
};

export const deleteAllCompleted = async (): Promise<void> => {
  try {
    await axios.delete(`${API_URL}/completed-books/delete-all/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
  } catch (error) {
    console.error('Ошибка при удалении всех прочитанных книг:', error);
    throw error;
  }
};
