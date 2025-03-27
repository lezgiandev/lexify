<script setup lang="ts">
defineProps<{
  logo: string
  title: string
  author: string
  isCompleted: boolean
  bookId: number
}>()

const emit = defineEmits(['add-to-completed', 'remove-from-completed'])
</script>

<template>
  <div class="p-4 bg-zinc-800 rounded-xl">
    <img :src="logo" class="w-full h-48 object-cover mb-4 rounded-xl"  alt=""/>
    <h3 class="text-2xl font-bold text-violet-500 font-main mb-2">{{ title }}</h3>
    <p class="text-white text-lg font-main mb-4">{{ author }}</p>

    <div class="mt-4 flex justify-between items-center gap-4 font-main">
      <button
        @click="$router.push({ name: 'book', params: { bookId: bookId } })"
        class="flex-1 py-2 px-6 bg-violet-500 text-white rounded-xl font-bold hover:bg-violet-700 shadow-lg transition-all"
      >
        Читать
      </button>

      <button
        v-if="isCompleted"
        @click="emit('remove-from-completed', bookId)"
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

      <button
        v-else
        @click="emit('add-to-completed', bookId)"
        class="p-2 rounded-xl shadow-lg hover:shadow-xl transition-all bg-violet-500/20 text-violet-500 hover:bg-violet-500 hover:text-button-text"
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
            d="M5 13l4 4L19 7"
          />
        </svg>
      </button>
    </div>
  </div>
</template>
