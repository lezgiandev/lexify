<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import { useRouter } from 'vue-router';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';

const username = ref('');
const password = ref('');
const authStore = useAuthStore();
const router = useRouter();

const login = async () => {
  await authStore.login({ username: username.value, password: password.value });
  await router.push('/');
};
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <div class="flex-grow container mx-auto px-4 py-12">
      <div class="max-w-md mx-auto bg-background-two rounded-3xl shadow-2xl p-8 relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-30"></div>

        <div class="relative z-10">
          <h1 class="text-4xl font-bold text-center mb-8 text-font-colored font-great">
            Добро пожаловать
            <span class="block text-2xl mt-2 font-main">Войдите в свой аккаунт</span>
          </h1>

          <form @submit.prevent="login" class="space-y-6">
            <div class="group relative">
              <input
                v-model="username"
                type="text"
                required
                class="w-full px-6 py-4 bg-background-three rounded-xl text-font-main
                       focus:outline-none focus:ring-2 focus:ring-button-main
                       border-2 border-transparent focus:border-button-main
                       transition-all duration-300 placeholder-transparent"
                placeholder=" "
              />
              <label class="absolute left-4 top-2 text-sm text-font-main opacity-75
                           group-focus-within:-translate-y-8 group-focus-within:scale-90
                           transition-all duration-300 pointer-events-none">
                Имя пользователя
              </label>
            </div>

            <div class="group relative">
              <input
                v-model="password"
                type="password"
                required
                class="w-full px-6 py-4 bg-background-three rounded-xl text-font-main
                       focus:outline-none focus:ring-2 focus:ring-button-main
                       border-2 border-transparent focus:border-button-main
                       transition-all duration-300 placeholder-transparent"
                placeholder=" "
              />
              <label class="absolute left-4 top-2 text-sm text-font-main opacity-75
                           group-focus-within:-translate-y-8 group-focus-within:scale-90
                           transition-all duration-300 pointer-events-none">
                Пароль
              </label>
            </div>

            <button
              type="submit"
              class="w-full px-6 py-4 bg-button-main text-button-text font-semibold rounded-xl
                    hover:bg-button-mainhover transition-all duration-300 shadow-lg hover:shadow-xl
                    flex items-center justify-center gap-2"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/>
              </svg>
              Войти
            </button>
          </form>

          <div class="mt-8 text-center">
            <router-link
              to="/register"
              class="text-button-main hover:underline font-main text-sm
                    inline-flex items-center gap-1"
            >
              Нет аккаунта? Зарегистрируйтесь
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
              </svg>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<style>
/* Анимация плавающих лейблов */
input:not(:placeholder-shown) + label {
  transform: translateY(-24px) scale(0.9);
  opacity: 1;
}

/* Кастомный плейсхолдер */
input::placeholder {
  color: transparent;
}
</style>
