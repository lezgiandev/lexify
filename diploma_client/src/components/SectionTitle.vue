<script setup lang="ts">
defineProps({
  text: String
})
</script>

<template>
  <h2 class="font-main text-4xl font-bold text-goldlight text-center mb-8 relative">
    <span class="absolute bottom-0 left-1/2 transform -translate-x-1/2 w-32 h-1 bg-darkfour"></span>
    {{ text }}
  </h2>
</template>
