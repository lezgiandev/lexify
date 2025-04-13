<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import { useRouter } from 'vue-router';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import  {useUserStore } from "@/stores/userStore.ts";
import CustomListbox from "@/components/CustomListbox.vue";
import PasswordInput from "@/components/PasswordInput.vue";

const username = ref('');
const password = ref('');
const confirmPassword = ref('');
const selectedLanguage = ref<number | null>(null);
const errorMessage = ref('');
const authStore = useAuthStore();
const router = useRouter();

const userStore = useUserStore();

const fetchLanguages = async () => {
  await userStore.fetchAllLanguages()
}

const register = async () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Пароли не совпадают';
    return;
  }

  if (!selectedLanguage.value) {
    errorMessage.value = 'Пожалуйста, выберите язык';
    return;
  }

  await authStore.register({
    username: username.value,
    password: password.value,
    language: selectedLanguage.value
  });
  await router.push('/login');
};

onMounted(
  async () => {
    await userStore.fetchAllLanguages()
  });
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <NavBar />
    <div class="flex-grow container mx-auto px-4 py-8">
      <div class="max-w-md mx-auto p-8">
        <h1 class="text-3xl font-bold text-center mb-8 text-light">Регистрация</h1>
        <form @submit.prevent="register" class="space-y-6">
          <div class="group relative">
            <input
              v-model="username"
              type="text"
              required
              class="w-full px-6 py-4 bg-darktwo rounded-xl text-light
                       focus:outline-none focus:ring-2 focus:ring-goldlight
                       border-2 border-transparent focus:border-goldlight
                       transition-all duration-300 placeholder-transparent"
              placeholder=" "
            />
            <label class="absolute left-4 top-1 text-sm text-light opacity-75
                           group-focus-within:-translate-y-7 group-focus-within:scale-90
                           transition-all duration-300 pointer-events-none">
              Имя пользователя
            </label>
          </div>

          <PasswordInput
            v-model="password"
            placeholder="Пароль"
            required
          />

          <PasswordInput
            v-model="confirmPassword"
            placeholder="Повторите пароль"
            required
          />

          <div class="group relative">
            <label class="block text-sm font-medium text-light">Выберите язык</label>
            <CustomListbox
              v-model="selectedLanguage"
              :options="userStore.languages"
              defaultLabel="Язык не выбран"
              @update:modelValue="fetchLanguages"
            />
          </div>

          <button
            type="submit"
            class="w-full px-6 py-4 bg-goldlight text-darkone font-semibold rounded-xl
                    hover:bg-golddark transition-all duration-300 shadow-lg hover:shadow-xl
                    flex items-center justify-center gap-2"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/>
            </svg>
            Зарегестрироваться
          </button>
        </form>
      </div>
    </div>
    <Footer />
  </div>
</template>
