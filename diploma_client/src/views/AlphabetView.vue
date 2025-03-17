<script setup lang="ts">
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import { useUserStore } from "@/stores/userStore";
import { useAlphabetStore } from "@/stores/alphabetStore";
import {onMounted} from "vue";

const userStore = useUserStore();
const alphabetStore = useAlphabetStore();

const playAudio = (audioUrl: string) => {
  if (audioUrl) {
    const audio = new Audio(audioUrl);
    audio.play();
  }
};

onMounted(async () => {
  await userStore.fetchUserLanguage();
  await alphabetStore.fetchAllLetters();
});
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <!-- Заголовок с акцентной линией -->
      <div class="mb-8 relative">
        <h1 class="text-font-main text-3xl font-bold font-great">
          Алфавит: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-48 h-1 bg-button-main mt-2"></span>
        </h1>
        <p class="text-font-colored text-lg mt-2 font-main">
          Изменить язык можно в <router-link to="/profile" class="text-button-main hover:underline">профиле</router-link>
        </p>
      </div>

      <!-- Сетка букв -->
      <div
        v-if="alphabetStore.letters.length > 0"
        class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-6 xl:grid-cols-8 2xl:grid-cols-10 gap-4"
      >
        <div
          v-for="letter in alphabetStore.letters"
          :key="letter.id"
          class="group relative p-6 bg-background-two rounded-2xl shadow-xl transition-all duration-300
               flex flex-col items-center justify-center aspect-square overflow-hidden"
        >
          <!-- Буква -->
          <span class="text-5xl md:text-6xl font-bold text-font-main mb-2 transition-transform">
            {{ letter.letter }}
          </span>

          <!-- Кнопка аудио -->
          <button
            @click="playAudio(letter.audio)"
            class="p-2 bg-button-main/10 text-button-main rounded-xl shadow-lg hover:shadow-xl hover:bg-button-main hover:text-button-text transition-all duration-300"
          >
            <svg
              class="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"
              />
            </svg>
          </button>
        </div>
      </div>

      <!-- Пустое состояние -->
      <div v-else class="text-center py-12">
        <div class="inline-flex flex-col items-center max-w-md mx-auto animate-fade-in">
          <div class="relative mb-6">
            <div class="w-32 h-32 bg-button-main/10 rounded-full animate-pulse"></div>
            <svg class="w-20 h-20 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-button-main"
                 fill="none"
                 stroke="currentColor"
                 viewBox="0 0 24 24">
              <path stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="1.5"
                    d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
            </svg>
          </div>
          <p class="text-font-main text-xl font-medium mb-4">
            Алфавит для выбранного языка пока недоступен
          </p>
        </div>
      </div>
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

.aspect-square {
  aspect-ratio: 1 / 1;
}
</style>
