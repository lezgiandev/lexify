import type { BookResponse, Sentence } from "@/types/types.ts";
import axios from "axios";
import { API_URL } from "@/services/baseURL.ts";


export const getBooks = async (params: {
  page?: number;
}): Promise<BookResponse> => {
  try {
    const response = await axios.get<BookResponse>(`${API_URL}/library/`, {
      params: {
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

