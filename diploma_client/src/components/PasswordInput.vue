<script setup lang="ts">
import { ref } from 'vue';

defineProps({
  modelValue: {
    type: String,
    required: true,
  },
  placeholder: {
    type: String,
    required: true,
  },
  required: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(['update:modelValue']);
const showPassword = ref(false);

const updateValue = (event: Event) => {
  emit('update:modelValue', (event.target as HTMLInputElement).value);
};
</script>

<template>
  <div class="group relative">
    <input
      :value="modelValue"
      :type="showPassword ? 'text' : 'password'"
      :required="required"
      class="w-full px-6 py-4 bg-darktwo rounded-xl text-light
        focus:outline-none focus:ring-2 focus:ring-goldlight
        border-2 border-transparent focus:border-goldlight
        transition-all duration-300 placeholder-transparent pr-12"
      placeholder=" "
      @input="updateValue"
    />
    <label class="absolute left-4 top-1 text-sm text-light opacity-75
         group-focus-within:-translate-y-7 group-focus-within:scale-90
         transition-all duration-300 pointer-events-none">
      {{ placeholder }}
    </label>

    <button
      type="button"
      @click="showPassword = !showPassword"
      class="absolute right-4 top-1/2 -translate-y-1/2 text-light/50 hover:text-light transition-colors"
      aria-label="Показать пароль"
    >
      <svg
        v-if="showPassword"
        class="w-6 h-6"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
        />
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
        />
      </svg>
      <svg
        v-else
        class="w-6 h-6"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"
        />
      </svg>
    </button>
  </div>
</template>
