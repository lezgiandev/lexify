<script setup lang="ts">
defineProps({
  title: String,
  description: String,
  tag: String
})
</script>

<template>
  <div class="bg-zinc-700 p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 group relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-br from-violet-500/10 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
    <div class="text-violet-500 mb-6">
      <slot name="icon" />
    </div>
    <h3 class="text-2xl font-bold text-violet-500 text-center mb-4">{{ title }}</h3>
    <p class="text-white text-center text-xl mb-4">
      {{ description }}
    </p>
    <div class="text-center">
      <span class="inline-block bg-violet-500/10 text-violet-500 px-3 py-1 rounded-full text-sm">{{ tag }}</span>
    </div>
  </div>
</template>
