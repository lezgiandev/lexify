<script setup lang="ts">
defineProps({
  title: String,
  description: String,
  tag: String
})
</script>

<template>
  <div class="bg-darkone p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 group relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-br from-goldlight/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
    <div class="text-goldlight mb-6">
      <slot name="icon" />
    </div>
    <h3 class="text-2xl font-bold text-goldlight text-center mb-4">{{ title }}</h3>
    <p class="text-light text-center text-xl mb-4">
      {{ description }}
    </p>
    <div class="text-center">
      <span class="inline-block bg-goldlight/10 text-goldlight px-3 py-1 rounded-full text-sm">{{ tag }}</span>
    </div>
  </div>
</template>
