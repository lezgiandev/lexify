<script setup lang="ts">
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import { useUserStore } from "@/stores/userStore";
import { useAlphabetStore } from "@/stores/alphabetStore";
import {onMounted} from "vue";
import EmptyState from "@/components/EmptyState.vue";
import LetterCard from "@/components/LetterCard.vue";

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
  <div class="min-h-screen flex flex-col bg-darkone">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <div class="mb-8 relative">
        <h1 class="text-light text-3xl font-bold font-main">
          Алфавит: {{ userStore.language?.name }}
          <span class="absolute bottom-0 left-0 w-48 h-1 bg-goldlight mt-2"></span>
        </h1>
        <p class="text-goldlight text-lg mt-2 font-main">
          Изменить язык можно в <router-link to="/settings" class="text-goldlight hover:underline">настройках</router-link>
        </p>
      </div>

      <div
        v-if="alphabetStore.letters.length > 0"
        class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-6 xl:grid-cols-8 2xl:grid-cols-10 gap-4"
      >
        <LetterCard
          v-for="letter in alphabetStore.letters"
          :key="letter.id"
          :letter="letter.letter"
          :audioUrl="letter.audio"
          :letterId="letter.id"
          @play-audio="playAudio"
        />
      </div>

      <EmptyState v-else>
        Алфавит для выбранного языка пока недоступен
      </EmptyState>
    </main>
    <Footer />
  </div>
</template>

<style>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
