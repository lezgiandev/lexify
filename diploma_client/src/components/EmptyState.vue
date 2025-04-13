<template>
  <div class="text-center py-12">
    <div class="inline-flex flex-col items-center max-w-md mx-auto animate-fade-in">
      <div class="relative mb-6">
        <div class="w-32 h-32 bg-goldlight/20 rounded-full animate-pulse"></div>
        <slot name="icon">
          <svg class="w-20 h-20 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-darkone"
               fill="none"
               stroke="currentColor"
               viewBox="0 0 24 24">
            <path stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.5"
                  d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
          </svg>
        </slot>
      </div>
      <p class="text-light text-xl font-bold mb-4">
        <slot></slot>
      </p>
    </div>
  </div>
</template>
