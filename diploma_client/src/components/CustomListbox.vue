<script setup lang="ts">
import { Listbox, ListboxButton, ListboxOptions, ListboxOption } from '@headlessui/vue'

defineProps<{
  modelValue: number | null
  options: Array<{ id: number; name: string }>
  defaultLabel: string
}>()

const emit = defineEmits<{
  'update:modelValue': [value: number | null]
}>()
</script>

<template>
  <Listbox
    :modelValue="modelValue"
    @update:modelValue="(value) => emit('update:modelValue', value)"
    v-slot="{ open }"
  >
    <div class="relative group">
      <ListboxButton
        class="w-full p-4 font-semibold bg-darktwo text-light rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 text-left pr-12"
      >
        {{ options.find(o => o.id === modelValue)?.name || defaultLabel }}
        <span class="absolute inset-y-0 right-4 flex items-center">
          <svg
            class="w-5 h-5 text-orange-300 transform transition duration-300"
            :class="{ 'rotate-180': open }"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
          </svg>
        </span>
      </ListboxButton>

      <ListboxOptions
        class="absolute z-20 w-full mt-2 bg-darktwo rounded-xl shadow-2xl max-h-60 overflow-y-auto"
      >
        <ListboxOption
          :value="null"
          v-slot="{ active }"
          class="cursor-default"
        >
          <li
            :class="[
              active ? 'bg-darkthree text-light' : 'bg-darktwo text-light',
              'p-3 font-semibold transition-colors'
            ]"
          >
            {{ defaultLabel }}
          </li>
        </ListboxOption>

        <ListboxOption
          v-for="option in options"
          :key="option.id"
          :value="option.id"
          v-slot="{ active }"
          class="cursor-default"
        >
          <li
            :class="[
              active ? 'bg-darkthree text-light' : 'bg-darktwo text-light',
              'p-3 font-semibold transition-colors'
            ]"
          >
            {{ option.name }}
          </li>
        </ListboxOption>
      </ListboxOptions>
    </div>
  </Listbox>
</template>
