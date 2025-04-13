<script setup lang="ts">
defineProps<{
  currentPage: number
  totalPages: number
}>()

const emit = defineEmits(['prev', 'next'])
</script>

<template>
  <div class="mt-8 flex justify-center gap-4 font-main">
    <button
      @click="emit('prev')"
      :disabled="currentPage === 1"
      class="px-6 py-3 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300"
      :class="currentPage === 1
        ? 'bg-darkthree text-font-main opacity-50 cursor-not-allowed'
        : 'bg-goldlight text-darkthree hover:bg-golddark'"
    >
      ← Назад
    </button>

    <div class="flex items-center bg-darktwo rounded-xl px-6 shadow-lg">
      <span class="text-light">
        Страница {{ currentPage }} <span class="opacity-50">из {{ totalPages }}</span>
      </span>
    </div>

    <button
      @click="emit('next')"
      :disabled="currentPage >= totalPages"
      class="px-6 py-3 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300"
      :class="currentPage >= totalPages
        ? 'bg-darkthree text-font-main opacity-50 cursor-not-allowed'
        : 'bg-goldlight text-darkthree hover:bg-golddark'"
    >
      Вперед →
    </button>
  </div>
</template>
