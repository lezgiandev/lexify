import type { MarkedSource } from "@/types/types.ts";
import axios from "axios";
import { API_URL } from "@/services/baseURL.ts";

export const getMarkedSources = async (): Promise<MarkedSource[]> => {
  try {
    const response = await axios.get<MarkedSource[]>(`${API_URL}/marked-sources/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении отмеченных источников:', error);
    throw error;
  }
};

export const addToMarkedSources = async (source_id: number): Promise<void> => {
  try {
    await axios.post(
      `${API_URL}/marked-sources/`,
      { source_id: source_id },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      }
    );
  } catch (error) {
    console.error('Ошибка при добавлении в отмеченное:', error);
    throw error;
  }
};

export const removeFromMarkedSources = async (source_id: number): Promise<void> => {
  try {
    await axios.delete(`${API_URL}/marked-sources/delete/`, {
      params: {
        source_id: source_id,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
  } catch (error) {
    console.error('Ошибка при удалении из отмеченного:', error);
    throw error;
  }
};
