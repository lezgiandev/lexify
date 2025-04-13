<script setup lang="ts">
defineProps({
  number: String,
  text: String
})
</script>

<template>
  <div class="bg-darkthree p-6 rounded-xl hover:transform hover:-translate-y-2 transition duration-300">
    <div class="text-5xl font-bold text-goldlight mb-4">{{ number }}</div>
    <p class="font-main text-light">{{ text }}</p>
  </div>
</template>
