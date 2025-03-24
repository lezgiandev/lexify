<script setup lang="ts">
import {onMounted, ref} from 'vue';
import { useTtsStore } from '@/stores/ttsStore';
import { useUserStore } from "@/stores/userStore.ts";
import { storeToRefs } from 'pinia';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import CustomAudioPlayer from "@/components/CustomAudioPlayer.vue";
import EmptyState from "@/components/EmptyState.vue";

const ttsStore = useTtsStore();
const userStore = useUserStore();

const { isLoading, error, history } = storeToRefs(ttsStore);
const inputText = ref('');

const generate = async () => {
  if (inputText.value.trim()) {
    await ttsStore.generateSpeech(inputText.value.trim());
  }
};

const clearHistory = () => {
  ttsStore.clearHistory();
};

const formatDate = (date: Date) => {
  return new Intl.DateTimeFormat('ru-RU', {
    hour: '2-digit',
    minute: '2-digit',
    day: 'numeric',
    month: 'long'
  }).format(date);
};

onMounted(async () => {
  await userStore.fetchUserLanguage();
});
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <div class="mb-8 relative">
        <h1 class="text-font-main text-3xl font-bold font-great">
          Озвучка текста: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-32 h-1 bg-button-main mt-2"></span>
        </h1>
        <p class="text-font-colored text-lg mt-2 font-main">
          Изменить язык можно в <router-link to="/settings" class="text-button-main hover:underline">настройках</router-link>
        </p>
      </div>

      <div class="mb-8 space-y-6">
        <div class="relative group">
          <textarea
            v-model="inputText"
            placeholder="Введите текст для озвучивания..."
            :disabled="isLoading"
            class="w-full p-6 bg-background-two text-font-main rounded-2xl shadow-xl focus:outline-none focus:ring-2 focus:ring-button-main font-main h-40 transition-all duration-300 hover:shadow-2xl resize-none pr-16"
          ></textarea>
          <div class="absolute bottom-6 right-6 flex gap-4">
            <button
              @click="generate"
              :disabled="!inputText || isLoading"
              class="px-6 py-3 bg-button-main text-button-text rounded-xl font-bold hover:bg-button-mainhover transition-all duration-300 flex items-center gap-2"
              :class="{ 'opacity-50 cursor-not-allowed': !inputText || isLoading }"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/>
              </svg>
              Озвучить
            </button>
          </div>
        </div>

        <div v-if="isLoading" class="flex items-center justify-center gap-4 text-button-main">
          <div class="animate-spin w-8 h-8 border-4 border-button-main border-t-transparent rounded-full"></div>
          <span class="font-main">Идет генерация аудио...</span>
        </div>
      </div>

      <div v-if="error" class="mb-8 p-6 bg-red-100/50 backdrop-blur-sm rounded-2xl border-2 border-red-200 animate-fade-in">
        <div class="flex items-center gap-4 text-red-500">
          <svg class="w-6 h-6 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
          <p class="font-main">{{ error }}</p>
        </div>
      </div>

      <div v-if="history.length" class="bg-background-two rounded-2xl p-6 shadow-xl">
        <div class="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
          <h2 class="text-font-main text-2xl font-bold font-main">
            История генераций
            <span class="text-button-main/50">({{ history.length }})</span>
          </h2>
          <button
            @click="clearHistory"
            class="px-6 py-3 bg-button-cancel/20 text-button-cancel rounded-xl font-bold hover:bg-button-cancel hover:text-button-text transition-all duration-300 flex items-center gap-2"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
            </svg>
            Очистить историю
          </button>
        </div>

        <div class="space-y-4">
          <CustomAudioPlayer
            v-for="(item, index) in history"
            :key="index"
            :src="item.audioUrl"
            :text="item.text"
            :date="formatDate(item.timestamp)"
          />
        </div>
      </div>

      <EmptyState v-else>
        <template #icon>
          <svg class="w-20 h-20 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-button-main" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19.114 5.636a9 9 0 010 12.728M16.463 8.288a5.25 5.25 0 010 7.424M6.75 8.25l4.72-4.72a.75.75 0 011.28.53v15.88a.75.75 0 01-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.01 9.01 0 012.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75"/>
          </svg>
        </template>
        Ваши аудиогенерации появятся здесь
      </EmptyState>
    </main>
    <Footer />
  </div>
</template>

<style>
.animate-fade-in {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
