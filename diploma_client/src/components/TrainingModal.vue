<script setup lang="ts">
import {ref, computed, onMounted} from 'vue';
import type { FavoriteWord } from '@/types/types.ts';

const props = defineProps<{
  words: FavoriteWord[];
}>();

const emit = defineEmits(['close']);

type TestType = 1 | 2 | 3;

const userAnswer = ref('');
const showResult = ref(false);
const currentTestType = ref<TestType>(1);
const remainingWords = ref<FavoriteWord[]>([]);
const currentWordInTest = ref<FavoriteWord | null>(null);

const currentWord = computed(() => currentWordInTest.value);

const questionText = computed(() => {
  if (!currentWord.value) return '';
  const translation = currentWord.value.translation;
  switch (currentTestType.value) {
    case 1:
      return `Напишите перевод слова: "${translation.word.text}"`;
    case 2:
      return `Напишите слово для перевода: "${translation.text}"`;
    case 3:
      return 'Напишите перевод услышанного слова';
    default:
      return '';
  }
});

const correctAnswer = computed(() => {
  if (!currentWord.value) return '';
  return currentTestType.value === 1
    ? currentWord.value.translation.text
    : currentWord.value.translation.word.text;
});

const playCurrentAudio = () => {
  if (!currentWord.value) return;
  const audioUrl = currentWord.value.translation.audio;
  if (audioUrl) {
    const audio = new Audio(audioUrl);
    audio.play();
  }
};

const startNewTest = () => {
  if (remainingWords.value.length === 0) {
    remainingWords.value = [...props.words];
  }

  const randomIndex = Math.floor(Math.random() * remainingWords.value.length);
  currentWordInTest.value = remainingWords.value[randomIndex];

  const translation = currentWordInTest.value.translation;
  const hasAudio = !!translation.audio;

  const availableTypes = [
    1,
    2,
    ...(hasAudio ? [3] : []),
  ] as TestType[];

  currentTestType.value = availableTypes[Math.floor(Math.random() * availableTypes.length)];
  userAnswer.value = '';
  showResult.value = false;

  if (currentTestType.value === 3) {
    playCurrentAudio();
  }
};

const checkAnswer = () => {
  showResult.value = true;
};

const nextWord = () => {
  if (showResult.value) {
    const isCorrect = userAnswer.value.trim().toLowerCase() === correctAnswer.value.toLowerCase();
    if (isCorrect && currentWordInTest.value) {
      const index = remainingWords.value.findIndex(word => word === currentWordInTest.value);
      if (index !== -1) {
        remainingWords.value.splice(index, 1);
      }
    }
  }
  startNewTest();
};

onMounted(() => {
  remainingWords.value = [...props.words];
  startNewTest();
});
</script>

<template>
  <div class="fixed inset-0 bg-black/80 flex items-center justify-center p-4 z-50">
    <div class="bg-zinc-800 rounded-2xl p-8 max-w-2xl w-full shadow-xl relative">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-white">Тренировка</h2>

        <button
          @click="emit('close')"
          class="absolute top-7 right-8 rounded-xl p-2 border-red-500 border text-red-500 hover:bg-red-500 hover:text-zinc-800 transition"
          aria-label="Закрыть"
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
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <div class="mb-6">
        <p class="text-xl text-white font-semibold mb-4">{{ questionText }}</p>

        <div v-if="currentTestType === 3" class="mb-4">
          <button
            @click="playCurrentAudio"
            class="py-3 px-6 bg-violet-500 text-slate-100 rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-violet-700 transition-all duration-300 flex items-center justify-center gap-2"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/>
            </svg>
            Озвучить
          </button>
        </div>

        <input
          v-model="userAnswer"
          :disabled="showResult"
          type="text"
          class="w-full p-3 rounded-xl bg-zinc-700 font-semibold text-white focus:ring-2 focus:ring-violet-500 focus:outline-none"
          placeholder="Введите ваш ответ..."
        />
      </div>

      <div v-if="showResult" class="mb-6 font-semibold bg-zinc-700 rounded-2xl p-4">
        <p
          class="text-xl font-semibold"
          :class="userAnswer.trim().toLowerCase() === correctAnswer.toLowerCase()
            ? 'text-green-500'
            : 'text-red-500'"
        >
          {{ userAnswer.trim().toLowerCase() === correctAnswer.toLowerCase()
          ? 'Правильно! 🎉'
          : 'Неверно 😞' }}
        </p>
        <p class="text-white mt-2 text-xl">
          Правильный ответ: <span class="font-bold">{{ correctAnswer }}</span>
        </p>
      </div>

      <div class="flex justify-end gap-4">
        <button
          v-if="!showResult"
          @click="checkAnswer"
          class="px-6 py-3 bg-violet-500 text-slate-100 rounded-xl font-bold hover:bg-violet-700 transition"
        >
          Проверить
        </button>

        <button
          v-else
          @click="nextWord"
          class="px-6 py-3 bg-violet-500 text-slate-100 rounded-xl font-bold hover:bg-violet-700 transition"
        >
          Далее
        </button>
      </div>
    </div>
  </div>
</template>
