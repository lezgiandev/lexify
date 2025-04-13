<script setup lang="ts">
import {ref} from "vue";
import DetailsModal from "@/components/DetailsModal.vue";

const props = defineProps<{
  word: string
  wordId: number
}>()

const showDetailsModal = ref(false);

const openDetails = () => {
  showDetailsModal.value = true;
};
</script>

<template>
  <div class="p-4 bg-darktwo rounded-2xl shadow-lg flex flex-row md:flex-row justify-between items-center">
    <div class="flex flex-grow space-x-4 w-full md:w-auto font-main">
      <div class="flex-1 text-xl rounded-lg text-light text-center whitespace-normal break-words font-bold">
        {{ word }}
      </div>
    </div>

    <div class="flex space-x-4 mt-0 ml-4 font-main">
      <button
        @click="openDetails"
        class="p-2 bg-goldlight/20 text-goldlight rounded-xl hover:bg-goldlight hover:text-darktwo transition duration-300"
      >
        <svg
          class="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M16 12m-7-7l7 7-7 7"
          />
        </svg>
      </button>
    </div>

    <DetailsModal
      v-if="showDetailsModal"
      :word="props.word"
      :wordId="Number(props.wordId)"
      @close="showDetailsModal = false"
    />
  </div>
</template>
