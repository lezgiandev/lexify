<script setup lang="ts">
defineProps({
  title: String,
  speakers: String,
  tags: Array,
  materials: String
})
</script>

<template>
  <div class="bg-zinc-800 p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-br from-violet-500/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
    <h3 class="text-2xl font-bold text-violet-500 text-center mb-4">{{ title }}</h3>
    <p class="text-white text-center text-xl mb-4">
      {{ speakers }}
    </p>
    <div class="flex flex-wrap justify-center gap-2">
      <span
        v-for="(tag, index) in tags"
        :key="index"
        class="bg-violet-500/10 text-violet-500 px-3 py-1 rounded-full text-sm"
      >
        {{ tag }}
      </span>
    </div>
    <div class="mt-4 text-center text-sm text-white opacity-80">
      {{ materials }}
    </div>
  </div>
</template>
