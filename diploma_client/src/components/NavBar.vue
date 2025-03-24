<template>
  <nav class="bg-navbar-main p-4">
    <div class="container mx-auto flex justify-between items-center">
      <router-link
        to="/"
        class="text-navbar-colored text-4xl lg:text-5xl font-great font-bold transition-transform duration-300"
      >
        Lexify
      </router-link>

      <button @click="toggleMobileMenu" class="text-navbar-colored lg:hidden focus:outline-none">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16m-7 6h7"
          ></path>
        </svg>
      </button>

      <div class="hidden lg:flex lg:items-center lg:space-x-6">
        <router-link
          to="/login"
          class="text-navbar-text hover:text-navbar-colored text-xl font-main"
          v-if="!authStore.isAuthenticated"
        >Вход</router-link>

        <router-link
          to="/register"
          class="text-navbar-text hover:text-navbar-colored text-xl font-main"
          v-if="!authStore.isAuthenticated"
        >Регистрация</router-link>

        <router-link
          to="/alphabet"
          class="text-navbar-text font-main hover:text-navbar-colored text-xl"
          v-if="authStore.isAuthenticated"
        >Алфавит</router-link>

        <router-link
          to="/tts"
          class="text-navbar-text font-main hover:text-navbar-colored text-xl"
          v-if="authStore.isAuthenticated"
        >Озвучка</router-link>

        <router-link
          to="/dictionary"
          class="text-navbar-text font-main hover:text-navbar-colored text-xl"
          v-if="authStore.isAuthenticated"
        >Словарь</router-link>

        <router-link
          to="/library"
          class="text-navbar-text font-main hover:text-navbar-colored text-xl"
          v-if="authStore.isAuthenticated"
        >Библиотека</router-link>

        <router-link
          to="/sources"
          class="text-navbar-text font-main hover:text-navbar-colored text-xl"
          v-if="authStore.isAuthenticated"
        >Источники</router-link>

        <router-link
          to="/settings"
          class="text-navbar-text font-main hover:text-navbar-colored text-xl"
          v-if="authStore.isAuthenticated"
        >Настройки</router-link>
      </div>
    </div>

    <div :class="['lg:hidden', isMobileMenuOpen ? 'block' : 'hidden', 'transition-all duration-300 ease-in-out']">
      <div class="px-4 py-6 space-y-4">
        <router-link
          to="/login"
          @click="isMobileMenuOpen = false"
          class="font-main block text-navbar-text text-xl hover:text-navbar-colored"
          v-if="!authStore.isAuthenticated"
        >Вход</router-link>

        <router-link
          to="/register"
          @click="isMobileMenuOpen = false"
          class="font-main block text-navbar-text text-xl hover:text-navbar-colored"
          v-if="!authStore.isAuthenticated"
        >Регистрация</router-link>

        <router-link
          to="/alphabet"
          @click="isMobileMenuOpen = false"
          class="font-main block text-navbar-text text-xl hover:text-navbar-colored"
          v-if="authStore.isAuthenticated"
        >Алфавит</router-link>

        <router-link
          to="/tts"
          @click="isMobileMenuOpen = false"
          class="font-main block text-navbar-text text-xl hover:text-navbar-colored"
          v-if="authStore.isAuthenticated"
        >Озвучка</router-link>

        <router-link
          to="/dictionary"
          @click="isMobileMenuOpen = false"
          class="font-main block text-navbar-text text-xl hover:text-navbar-colored"
          v-if="authStore.isAuthenticated"
        >Словарь</router-link>

        <router-link
          to="/library"
          @click="isMobileMenuOpen = false"
          class="font-main block text-navbar-text text-xl hover:text-navbar-colored"
          v-if="authStore.isAuthenticated"
        >Библиотека</router-link>

        <router-link
          to="/sources"
          @click="isMobileMenuOpen = false"
          class="font-main block text-navbar-text text-xl hover:text-navbar-colored"
          v-if="authStore.isAuthenticated"
        >Источники</router-link>

        <router-link
          to="/settings"
          @click="isMobileMenuOpen = false"
          class="font-main block text-navbar-text text-xl hover:text-navbar-colored"
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
