import { defineStore } from 'pinia';
import ttsService from '@/services/ttsService';

interface TtsState {
  isLoading: boolean;
  error: string | null;
  audioBlob: Blob | null;
  history: Array<{
    text: string;
    audioUrl: string;
    timestamp: Date;
  }>;
}

export const useTtsStore = defineStore('tts', {
  state: (): TtsState => ({
    isLoading: false,
    error: null,
    audioBlob: null,
    history: []
  }),
  actions: {
    async generateSpeech(text: string) {
      try {
        this.isLoading = true;
        this.error = null;

        const audioData = await ttsService.generateSpeech(text);
        const blob = new Blob([audioData], { type: 'audio/wav' });

        // Сохраняем в историю
        const audioUrl = URL.createObjectURL(blob);
        this.history.unshift({
          text,
          audioUrl,
          timestamp: new Date()
        });

        this.audioBlob = blob;
      } catch (error) {
        this.error = (error as Error).message || 'Ошибка генерации речи';
      } finally {
        this.isLoading = false;
      }
    },
    clearHistory() {
      this.history = [];
    }
  },
  getters: {
    audioUrl(): string | null {
      return this.audioBlob ? URL.createObjectURL(this.audioBlob) : null;
    }
  }
});
