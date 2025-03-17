<script setup lang="ts">
import {onMounted, ref, watch} from 'vue';

const props = defineProps({
  src: {
    type: String,
    required: true
  },
  text: {
    type: String,
    default: ''
  },
  date: {
    type: String,
    default: ''
  },
});

const audioElement = ref<HTMLAudioElement | null>(null);
const isPlaying = ref(false);
const currentTime = ref(0);
const duration = ref(0);
const volume = ref(1);
const progress = ref(0);

const formatTime = (seconds: number) => {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = Math.floor(seconds % 60);
  return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
};

const togglePlay = () => {
  if (!audioElement.value) return;

  if (isPlaying.value) {
    audioElement.value.pause();
  } else {
    audioElement.value.play();
  }
};

const handleProgressChange = (e: Event) => {
  if (!audioElement.value) return;
  const target = e.target as HTMLInputElement;
  audioElement.value.currentTime = (Number(target.value) / 100) * duration.value;
};

const handleVolumeChange = (e: Event) => {
  if (!audioElement.value) return;
  const target = e.target as HTMLInputElement;
  volume.value = Number(target.value) / 100;
  audioElement.value.volume = volume.value;
};

const downloadAudio = () => {
  const link = document.createElement('a');
  link.href = props.src;
  link.download = `audio-${Date.now()}.mp3`;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

onMounted(() => {
  if (audioElement.value) {
    audioElement.value.volume = volume.value;

    audioElement.value.addEventListener('timeupdate', () => {
      if (audioElement.value) {
        currentTime.value = audioElement.value.currentTime;
        progress.value = (currentTime.value / duration.value) * 100;
      }
    });

    audioElement.value.addEventListener('loadedmetadata', () => {
      if (audioElement.value) {
        duration.value = audioElement.value.duration;
      }
    });

    audioElement.value.addEventListener('play', () => {
      isPlaying.value = true;
    });

    audioElement.value.addEventListener('pause', () => {
      isPlaying.value = false;
    });
  }
});

watch(() => props.src, () => {
  if (audioElement.value) {
    audioElement.value.load();
    isPlaying.value = false;
    currentTime.value = 0;
    progress.value = 0;
  }
});
</script>

<template>
  <div class="bg-background-three rounded-xl p-4 shadow-xl space-y-2">
    <audio ref="audioElement" :src="src" hidden />

    <div class="flex flex-col sm:flex-row sm:justify-between gap-1 sm:gap-2">
      <p class="text-font-main font-medium line-clamp-2 flex-1 text-base">
        {{ text }}
      </p>
      <p class="text-sm text-font-main opacity-75 font-mono">
        {{ date }}
      </p>
    </div>

    <div class="flex items-center gap-4">
      <div
        @click="togglePlay"
        class="p-2 text-font-main hover:text-button-main cursor-pointer transition-colors"
        title="Воспроизвести/Пауза"
      >
        <svg
          class="w-6 h-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path v-if="!isPlaying"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.5"
                d="M5.25 5.653c0-.856.917-1.398 1.667-.986l11.54 6.347a1.125 1.125 0 0 1 0 1.972l-11.54 6.347a1.125 1.125 0 0 1-1.667-.986V5.653Z"
          />
          <path v-else
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.5"
                d="M15.75 5.25v13.5m-7.5-13.5v13.5"
          />
        </svg>
      </div>

      <div class="sm:flex-1 max-sm:hidden">
        <input
          type="range"
          :value="progress"
          @input="handleProgressChange"
          class="w-full h-2 rounded-lg appearance-none cursor-pointer progress-slider"
          :style="{
            background: `linear-gradient(to right, rgb(253 186 116) ${progress}%, rgb(38 38 38) ${progress}%)`
          }"
        />
      </div>

      <div class="flex gap-2 text-sm text-font-main">
        <span>{{ formatTime(currentTime) }}</span>
        <span>/</span>
        <span>{{ formatTime(duration) }}</span>
      </div>

      <div class="items-center gap-2 sm:flex max-sm:hidden">
        <svg class="w-5 h-5 text-font-main" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19.114 5.636a9 9 0 010 12.728M16.463 8.288a5.25 5.25 0 010 7.424M6.75 8.25l4.72-4.72a.75.75 0 011.28.53v15.88a.75.75 0 01-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.01 9.01 0 012.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75"/>
        </svg>

        <input
          type="range"
          min="0"
          max="100"
          :value="volume * 100"
          @input="handleVolumeChange"
          class="w-24 h-2 rounded-lg appearance-none cursor-pointer volume-slider"
          :style="{
          background: `linear-gradient(to right, rgb(253 186 116) ${volume * 100}%, rgb(38 38 38) ${volume * 100}%)`
        }"
        />
      </div>

      <button
        @click="downloadAudio"
        class="p-2 text-font-main hover:text-button-main transition-colors"
        title="Скачать аудио"
      >
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 12L12 16.5m0 0L7.5 12m4.5 4.5V3"/>
        </svg>
      </button>
    </div>
  </div>
</template>

<style scoped>
.progress-slider::-webkit-slider-thumb {
  @apply w-4 h-4 bg-button-main rounded-full appearance-none transition-all;
}

.progress-slider::-moz-range-thumb {
  @apply w-4 h-4 bg-button-main rounded-full transition-all;
}

.progress-slider::-webkit-slider-thumb:hover {
  @apply bg-button-mainhover shadow-md;
}

.progress-slider::-moz-range-track {
  @apply h-2 bg-background-three rounded-lg;
}

.volume-slider::-webkit-slider-thumb {
  @apply w-3 h-3 bg-button-main rounded-full appearance-none transition-all;
}

.volume-slider::-moz-range-thumb {
  @apply w-3 h-3 bg-button-main rounded-full transition-all;
}

.volume-slider::-webkit-slider-thumb:hover {
  @apply bg-button-mainhover shadow-md;
}

.volume-slider::-moz-range-track {
  @apply h-2 rounded-lg;
}
</style>
