<template>
  <nav class="bg-darktwo p-2">
    <div class="container mx-auto flex justify-between items-center">
      <router-link
        to="/"
        class="text-light text-2xl lg:text-5xl font-semibold font-great p-2"
      >
        Lexify
      </router-link>

      <button @click="toggleMobileMenu" class="text-light lg:hidden focus:outline-none">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16m-7 6h7"
          ></path>
        </svg>
      </button>

      <div class="hidden lg:flex lg:items-center lg:space-x-6 font-semibold">
        <router-link
          to="/login"
          class="text-light hover:text-golddark text-xl font-main"
          v-if="!authStore.isAuthenticated"
        >Вход</router-link>

        <router-link
          to="/register"
          class="text-light hover:text-golddark text-xl font-main"
          v-if="!authStore.isAuthenticated"
        >Регистрация</router-link>

        <router-link
          to="/alphabet"
          class="text-light font-main hover:text-golddark text-xl"
          v-if="authStore.isAuthenticated"
        >Алфавит</router-link>

        <router-link
          to="/tts"
          class="text-light font-main hover:text-golddark text-xl"
          v-if="authStore.isAuthenticated"
        >Озвучка</router-link>

        <router-link
          to="/dictionary"
          class="text-light font-main hover:text-golddark text-xl"
          v-if="authStore.isAuthenticated"
        >Словарь</router-link>

        <router-link
          to="/library"
          class="text-light font-main hover:text-golddark text-xl"
          v-if="authStore.isAuthenticated"
        >Библиотека</router-link>

        <router-link
          to="/sources"
          class="text-light font-main hover:text-golddark text-xl"
          v-if="authStore.isAuthenticated"
        >Источники</router-link>

        <router-link
          to="/settings"
          class="text-light font-main hover:text-golddark text-xl"
          v-if="authStore.isAuthenticated"
        >Настройки</router-link>
      </div>
    </div>

    <div :class="['lg:hidden', isMobileMenuOpen ? 'block' : 'hidden', 'transition-all duration-300 ease-in-out']">
      <div class="px-4 py-6 space-y-4">
        <router-link
          to="/login"
          @click="isMobileMenuOpen = false"
          class="font-main block text-light text-xl hover:text-golddark"
          v-if="!authStore.isAuthenticated"
        >Вход</router-link>

        <router-link
          to="/register"
          @click="isMobileMenuOpen = false"
          class="font-main block text-light text-xl hover:text-golddark"
          v-if="!authStore.isAuthenticated"
        >Регистрация</router-link>

        <router-link
          to="/alphabet"
          @click="isMobileMenuOpen = false"
          class="font-main block text-light text-xl hover:text-golddark"
          v-if="authStore.isAuthenticated"
        >Алфавит</router-link>

        <router-link
          to="/tts"
          @click="isMobileMenuOpen = false"
          class="font-main block text-light text-xl hover:text-golddark"
          v-if="authStore.isAuthenticated"
        >Озвучка</router-link>

        <router-link
          to="/dictionary"
          @click="isMobileMenuOpen = false"
          class="font-main block text-light text-xl hover:text-golddark"
          v-if="authStore.isAuthenticated"
        >Словарь</router-link>

        <router-link
          to="/library"
          @click="isMobileMenuOpen = false"
          class="font-main block text-light text-xl hover:text-golddark"
          v-if="authStore.isAuthenticated"
        >Библиотека</router-link>

        <router-link
          to="/sources"
          @click="isMobileMenuOpen = false"
          class="font-main block text-light text-xl hover:text-golddark"
          v-if="authStore.isAuthenticated"
        >Источники</router-link>

        <router-link
          to="/settings"
          @click="isMobileMenuOpen = false"
          class="font-main block text-light text-xl hover:text-golddark"
          v-if="authStore.isAuthenticated"
        >Настройки</router-link>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';

const authStore = useAuthStore();
const isMobileMenuOpen = ref(false);

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};
</script>
