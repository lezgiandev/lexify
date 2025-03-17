import axios from "axios";
import { API_URL } from "@/services/baseURL.ts";

const ttsApi = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  responseType: 'arraybuffer'
});

ttsApi.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default {
  async generateSpeech(text: string): Promise<ArrayBuffer> {
    const response = await ttsApi.post('/generate-audio/', { text });
    return response.data;
  }
};
