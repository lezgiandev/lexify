<script setup lang="ts">
defineProps<{
  modelValue: string
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const handleInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target) {
    emit('update:modelValue', target.value)
  }
}
</script>

<template>
  <div class="relative group">
    <input
      :value="modelValue"
      @input="handleInput"
      type="text"
      placeholder="Поиск..."
      class="w-full p-4 bg-darktwo text-light font-semibold rounded-xl focus:outline-none focus:ring-2 focus:ring-goldlight shadow-lg hover:shadow-xl transition-all duration-300 pr-12"
    />
    <svg class="w-5 h-5 absolute right-4 top-4 text-goldlight opacity-70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
    </svg>
  </div>
</template>
