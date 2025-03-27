<script setup lang="ts">
defineProps<{
  letter: string
  audioUrl: string
  letterId: number
}>()

const emit = defineEmits(['play-audio'])
</script>

<template>
  <div class="group relative p-6 bg-zinc-800 rounded-2xl shadow-xl transition-all duration-300 flex flex-col items-center justify-center aspect-square overflow-hidden">
    <span class="text-4xl md:text-5xl font-bold text-white mb-2 transition-transform">
      {{ letter }}
    </span>

    <button
      @click="emit('play-audio', audioUrl)"
      class="p-2 bg-violet-500/20 text-violet-500 rounded-xl shadow-lg hover:shadow-xl hover:bg-violet-500 hover:text-button-text transition-all duration-300"
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
</template>
