<script setup lang="ts">
import { useDictionaryStore } from "@/stores/dictionaryStore.ts";
import { onMounted } from "vue";
import { useFavoriteWordStore } from "@/stores/favoriteWordStore.ts";

const props = defineProps<{
  word: string
  wordId: number
}>()
const emit = defineEmits(['close']);

const favoriteWordStore = useFavoriteWordStore();
const dictionaryStore = useDictionaryStore();

const playAudio = (audioUrl: string) => {
  if (audioUrl) {
    const audio = new Audio(audioUrl);
    audio.play();
  }
};

const addToFavorites = async (translationId: number) => {
  await favoriteWordStore.addFavorite(translationId);
};

const removeFromFavorites = async (translationId: number) => {
  await favoriteWordStore.removeFavorite(translationId);
};

const isFavorite = (translationId: number) => {
  return favoriteWordStore.isFavorite(translationId);
};

onMounted(async () => {
  if (props.wordId) {
    await dictionaryStore.fetchWordTranslations(props.wordId)
    await favoriteWordStore.fetchFavorites()
  }
})
</script>

<template>
  <div class="fixed inset-0 bg-darkone/50 flex items-center justify-center backdrop-blur-sm p-4 z-50">
    <div class="bg-darktwo rounded-2xl p-8 max-w-2xl w-full shadow-xl relative">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-light">Детали слова: {{ word }}</h2>

        <button
          @click="emit('close')"
          class="absolute top-7 right-8 rounded-xl p-2 border-redlight border text-redlight hover:bg-redlight hover:text-darktwo transition"
          aria-label="Закрыть"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <div v-if="dictionaryStore.currentWordTranslations.length > 0" class="grid grid-cols-1 gap-4 mb-6">
        <div
          class="p-4 bg-darkthree rounded-2xl shadow-lg flex flex-row md:flex-row justify-between items-center"
          v-for="translation in dictionaryStore.currentWordTranslations"
          :key="translation.id"
        >
          <div class="flex flex-grow space-x-4 w-full md:w-auto font-main">
            <div class="flex-1 text-xl rounded-lg text-light text-center whitespace-normal break-words font-bold">
              {{ translation.text }}
            </div>
          </div>

          <div class="flex space-x-4 mt-0 ml-4 font-main">
            <button
              @click="playAudio(translation.audio)"
              class="p-2 bg-goldlight/20 text-goldlight rounded-xl hover:bg-goldlight hover:text-darkthree transition duration-300"
            >
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"
                />
              </svg>
            </button>

            <button
              v-if="!isFavorite(translation.id)"
              @click="addToFavorites(translation.id)"
              class="p-2 rounded-xl transition duration-300 bg-goldlight/20 text-goldlight hover:bg-goldlight hover:text-darkthree"
            >
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                />
              </svg>
            </button>

            <button
              v-else
              @click="removeFromFavorites(translation.id)"
              class="p-2 rounded-xl transition duration-300 bg-redlight/20 text-redlight hover:bg-redlight hover:text-darkthree"
            >
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
