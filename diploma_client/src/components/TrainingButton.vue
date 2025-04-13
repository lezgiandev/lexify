<template>
  <router-link
    to="/training"
    class="p-4 bg-goldlight text-darkone rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-golddark transition-all duration-300 flex items-center justify-center gap-2"
  >
    <slot name="icon">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
      </svg>
    </slot>
    <slot>Заучивание</slot>
  </router-link>
</template>
