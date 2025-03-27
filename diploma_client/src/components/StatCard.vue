<script setup lang="ts">
defineProps({
  number: String,
  text: String
})
</script>

<template>
  <div class="bg-zinc-700 p-6 rounded-xl hover:transform hover:-translate-y-2 transition duration-300">
    <div class="text-5xl font-bold text-violet-500 mb-4">{{ number }}</div>
    <p class="font-main text-white">{{ text }}</p>
  </div>
</template>
