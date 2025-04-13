import type {
  SourceCategory,
  SourceResponse
} from "@/types";
import axios from "axios";
import { API_URL } from "@/services/baseURL.ts";

export const getSources = async (params: {
  category?: number;
  search?: string;
  page?: number;
}): Promise<SourceResponse> => {
  try {
    const response = await axios.get<SourceResponse>(`${API_URL}/sources/`, {
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
    console.error('Ошибка при получении источников:', error);
    throw error;
  }
};

export const getCategories = async (): Promise<SourceCategory[]> => {
  try {
    const response = await axios.get<SourceCategory[]>(`${API_URL}/source-categories/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении категорий источников:', error);
    throw error;
  }
};
