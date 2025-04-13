<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useLibraryStore } from '@/stores/libraryStore';
import { computed, onMounted, ref } from 'vue';
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";

const libraryStore = useLibraryStore();
const route = useRoute();
const showTranslate = ref<Record<number, boolean>>({});

const currentBook = computed(() =>
  libraryStore.books.find(b => b.id === Number(route.params.bookId))
);

const playAudio = (audioUrl: string) => {
  if (audioUrl) new Audio(audioUrl).play();
};

const toggleTranslate = (sentenceId: number) => {
  showTranslate.value = {
    ...showTranslate.value,
    [sentenceId]: !showTranslate.value[sentenceId]
  };
};

onMounted(async () => {
  await libraryStore.fetchBookSentences(Number(route.params.bookId));
});
</script>

<template>
  <div class="min-h-screen flex flex-col bg-darkone">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <div class="mb-8 relative">
        <h2 class="text-light text-4xl font-bold font-main">
          {{ currentBook?.title }}
          <span class="absolute bottom-0 left-0 w-48 h-1 bg-goldlight mt-2"></span>
        </h2>
        <p class="text-goldlight text-lg mt-4 font-main">{{ currentBook?.author }}</p>
      </div>

      <div class="mb-8 grid grid-cols-1 md:grid-cols-4 gap-4 font-main">
        <button
          @click="$router.go(-1)"
          class="p-4 bg-goldlight text-light rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-golddark transition-all duration-300 flex items-center justify-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
          </svg>
          Назад к библиотеке
        </button>
      </div>

      <div class="space-y-4">
        <div
          v-for="sentence in libraryStore.currentBookSentences"
          :key="sentence.id"
          class="group p-4 bg-darktwo rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 relative overflow-hidden"
        >
          <div class="flex flex-wrap items-center justify-between gap-4 relative">
            <p class="text-light text-lg font-medium flex-1 min-w-[200px] leading-relaxed">
              {{ sentence.text }}
            </p>

            <div class="flex items-center gap-3">
              <button
                @click="toggleTranslate(sentence.id)"
                class="p-2 rounded-xl bg-goldlight/20 text-goldlight hover:bg-goldlight hover:text-darktwo transition-all duration-300"
              >
                <svg
                  :class="{'rotate-180': showTranslate[sentence.id]}"
                  class="w-6 h-6 transition-transform duration-300"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M19 9l-7 7-7-7"
                  />
                </svg>
              </button>

              <button
                @click="playAudio(sentence.audio)"
                class="p-2 rounded-xl bg-goldlight/20 text-goldlight hover:bg-goldlight hover:text-darktwo transition-all duration-300"
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

          <transition
            enter-active-class="transition-all duration-300 ease-out"
            leave-active-class="transition-all duration-200 ease-in"
            enter-from-class="opacity-0 max-h-0"
            enter-to-class="opacity-100 max-h-40"
            leave-from-class="opacity-100 max-h-40"
            leave-to-class="opacity-0 max-h-0"
          >
            <div
              v-if="showTranslate[sentence.id]"
              class="mt-4 pl-4 border-l-4 border-goldlight/50 bg-darkthree/30 rounded-r-xl p-4"
            >
              <p class="text-goldlight text-lg font-medium leading-relaxed whitespace-pre-line">
                {{ sentence.translate }}
              </p>
            </div>
          </transition>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>
