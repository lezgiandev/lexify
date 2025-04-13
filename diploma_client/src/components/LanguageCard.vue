<script setup lang="ts">
defineProps({
  title: String,
  speakers: String,
  tags: Array,
  materials: String
})
</script>

<template>
  <div class="bg-darktwo p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-br from-goldlight/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
    <h3 class="text-2xl font-bold text-goldlight text-center mb-4">{{ title }}</h3>
    <p class="text-light text-center text-xl mb-4">
      {{ speakers }}
    </p>
    <div class="flex flex-wrap justify-center gap-2">
      <span
        v-for="(tag, index) in tags"
        :key="index"
        class="bg-goldlight/10 text-goldlight px-3 py-1 rounded-full text-sm"
      >
        {{ tag }}
      </span>
    </div>
    <div class="mt-4 text-center text-sm text-light opacity-80">
      {{ materials }}
    </div>
  </div>
</template>
