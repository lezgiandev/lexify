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
  <div class="p-4 bg-darktwo rounded-xl">
    <img :src="logo" class="w-full h-48 object-cover mb-4 rounded-xl"  alt=""/>
    <h3 class="text-2xl font-bold text-goldlight font-main mb-2">{{ title }}</h3>
    <p class="text-light text-lg font-main mb-4">{{ author }}</p>

    <div class="mt-4 flex justify-between items-center gap-4 font-main">
      <button
        @click="$router.push({ name: 'book', params: { bookId: bookId } })"
        class="flex-1 py-2 px-6 bg-goldlight text-darktwo rounded-xl font-bold hover:bg-golddark shadow-lg transition-all"
      >
        Читать
      </button>

      <button
        v-if="isCompleted"
        @click="emit('remove-from-completed', bookId)"
        class="p-2 rounded-xl shadow-lg hover:shadow-xl transition-all bg-redlight/20 text-redlight hover:bg-redlight hover:text-darktwo"
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
        class="p-2 rounded-xl shadow-lg hover:shadow-xl transition-all bg-goldlight/20 text-goldlight hover:bg-goldlight hover:text-darktwo"
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
