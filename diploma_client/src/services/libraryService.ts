import type {BookCategory, BookResponse, Sentence } from "@/types";
import axios from "axios";
import { API_URL } from "@/services/baseURL.ts";


export const getBooks = async (params: {
  category?: number;
  search?: string;
  page?: number;
}): Promise<BookResponse> => {
  try {
    const response = await axios.get<BookResponse>(`${API_URL}/library/`, {
      params: {
        category: params.category,
        search: params.search,
        page: params.page,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении книг:', error);
    throw error;
  }
};


export const getBookSentences = async (bookId: number, params: {
  page?: number;
}): Promise<Sentence[]> => {
  try {
    const response = await axios.get<Sentence[]>(`${API_URL}/library/${bookId}/sentences/`, {
      params: {
        page: params.page,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении предложений:', error);
    throw error;
  }
};


export const getCategories = async (): Promise<BookCategory[]> => {
  try {
    const response = await axios.get<BookCategory[]>(`${API_URL}/library-categories/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении категорий книг:', error);
    throw error;
  }
};
