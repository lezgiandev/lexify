<script setup lang="ts">
defineProps<{
  word: string
  translation: string
  audioUrl: string
  isFavorite: boolean
  translationId: number
}>()

const emit = defineEmits(['play-audio', 'add-to-favorite', 'remove-from-favorite'])
</script>

<template>
  <div class="p-6 bg-background-two rounded-2xl shadow-lg flex flex-col md:flex-row justify-between items-center">
    <div class="flex flex-grow space-x-4 w-full md:w-auto font-main">
      <div class="flex-1 p-2 rounded-lg bg-background-three text-font-main text-center truncate font-semibold">
        {{ word }}
      </div>
      <div class="text-font-main self-center text-2xl">→</div>
      <div class="flex-1 p-2 rounded-lg bg-background-three text-font-main text-center truncate font-semibold">
        {{ translation }}
      </div>
    </div>

    <div class="flex space-x-4 mt-4 md:mt-0 md:ml-4 font-main">
      <button
        @click="emit('play-audio', audioUrl)"
        class="p-2 bg-button-main/20 text-button-main rounded-xl hover:bg-button-main hover:text-button-text transition duration-300"
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
        v-if="!isFavorite"
        @click="emit('add-to-favorite', translationId)"
        class="p-2 rounded-xl transition duration-300 bg-button-main/20 text-button-main hover:bg-button-main hover:text-button-text"
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
        @click="emit('remove-from-favorite', translationId)"
        class="p-2 rounded-xl transition duration-300 bg-button-cancel/20 text-button-cancel hover:bg-button-cancel hover:text-button-text"
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
</template>
