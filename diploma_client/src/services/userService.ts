import axios from "axios";
import { API_URL } from "@/services/baseURL.ts";
import type { Language } from "@/types/types.ts";


export const getUserLanguage = async (): Promise<Language> => {
  try {
    const response = await axios.get<Language>(`${API_URL}/check-language/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении языка:', error);
    throw error;
  }
};

export const getAllLanguages = async (): Promise<Language[]> => {
  try {
    const response = await axios.get<Language[]>(`${API_URL}/languages/`);
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении языков:', error);
    throw error;
  }
};

export const updateUserLanguage = async (languageId: number): Promise<void> => {
  try {
    await axios.put(
      `${API_URL}/user/change-language/`,
      { language_id: languageId },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
          'Content-Type': 'application/json'
        }
      }
    );
  } catch (error) {
    console.error('Ошибка при изменении языка:', error);
    throw error;
  }
};
