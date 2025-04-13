import type { Letter } from "@/types";
import axios from "axios";
import { API_URL } from "@/services/baseURL.ts";

export const getLetters = async (): Promise<Letter[]> => {
  try {
    const response = await axios.get<Letter[]>(`${API_URL}/alphabet/`, {
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
