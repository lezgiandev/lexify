import axios from 'axios';
import { API_URL } from "@/services/baseURL.ts";

export const loginUser = async (credentials: { username: string; password: string }) => {
  const response = await axios.post(`${API_URL}/token/`, credentials);
  return response.data;
};

export const registerUser = async (userData: { username: string; password: string; language: number }) => {
  const response = await axios.post(`${API_URL}/register/`, userData);
  return response.data;
};
