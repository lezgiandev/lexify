<script setup lang="ts">
defineProps<{
  text: string
  link: string
  isMarked: boolean
  sourceId: number
}>()

const emit = defineEmits(['add-to-marked', 'remove-from-marked'])
</script>

<template>
  <div class="p-4 bg-zinc-800 rounded-2xl shadow-lg flex flex-col md:flex-row justify-between items-center">
    <div class="flex flex-grow space-x-4 w-full md:w-auto font-main">
      <h3 class="text-white text-xl font-medium truncate">{{ text }}</h3>
    </div>

    <div class="flex space-x-4 mt-4 md:mt-0 md:ml-4 font-main">
      <a
        :href="link"
        target="_blank"
        class="px-6 py-2 bg-violet-500 text-white rounded-xl font-semibold hover:bg-violet-700 shadow-lg hover:shadow-xl transition-all flex items-center gap-2"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
        Перейти
      </a>

      <button
        v-if="!isMarked"
        @click="emit('add-to-marked', sourceId)"
        class="p-2 rounded-xl shadow-lg hover:shadow-xl transition-all bg-violet-500/20 text-violet-500 hover:bg-violet-500 hover:text-zinc-800"
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
        @click="emit('remove-from-marked', sourceId)"
        class="p-2 rounded-xl shadow-lg hover:shadow-xl transition-all bg-button-cancel/20 text-button-cancel hover:bg-button-cancel hover:text-button-text"
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
