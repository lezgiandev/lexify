<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import { useRouter } from 'vue-router';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import { Listbox, ListboxButton, ListboxOption, ListboxOptions } from "@headlessui/vue";
import  {useUserStore } from "@/stores/userStore.ts";

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
      <div class="max-w-md mx-auto bg-background-two rounded-lg shadow-lg p-8">
        <h1 class="text-3xl font-bold text-center mb-8 text-font-colored">Регистрация</h1>
        <form @submit.prevent="register" class="space-y-6">
          <div class="mb-4">
            <label class="block text-sm font-medium text-font-main">Имя пользователя</label>
            <input v-model="username" type="text" class="mt-1 block w-full px-4 py-2 bg-background-three border border-font-main rounded-lg text-font-main focus:outline-none focus:ring-2 focus:ring-button-main" required />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-font-main">Пароль</label>
            <input v-model="password" type="password" class="mt-1 block w-full px-4 py-2 bg-background-three border border-font-main rounded-lg text-font-main focus:outline-none focus:ring-2 focus:ring-button-main" required />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-font-main">Подтвердите пароль</label>
            <input v-model="confirmPassword" type="password" class="mt-1 block w-full px-4 py-2 bg-background-three border border-font-main rounded-lg text-font-main focus:outline-none focus:ring-2 focus:ring-button-main" required />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-font-main">Выберите язык</label>

            <Listbox v-model="selectedLanguage" @update:modelValue="fetchLanguages">
              <div class="relative w-full font-main">

                <ListboxButton
                  class="w-full p-3 bg-background-three border-font-main text-font-main rounded-lg focus:outline-none focus:ring-2 focus:ring-button-main text-left appearance-none pr-10"
                >
                  {{ userStore.languages.find(l => l.id === selectedLanguage)?.name || 'Язык не выбран' }}

                  <span class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                <svg class="w-5 h-5 text-button-main" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
                </ListboxButton>

                <ListboxOptions
                  class="absolute z-10 w-full mt-1 bg-background-two rounded-lg shadow-lg focus:outline-none max-h-60 overflow-auto"
                >

                  <ListboxOption
                    :value="null"
                    v-slot="{ active }"
                    class="cursor-default"
                  >
                    <li
                      :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-three text-font-main',
                    'p-3 transition-colors'
                  ]"
                    >
                      Язык не выбран
                    </li>
                  </ListboxOption>

                  <ListboxOption
                    v-for="language in userStore.languages"
                    :key="language.id"
                    :value="language.id"
                    v-slot="{ active }"
                    class="cursor-default"
                  >
                    <li
                      :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-three text-font-main',
                    'p-3 transition-colors'
                  ]"
                    >
                      {{ language.name }}
                    </li>
                  </ListboxOption>
                </ListboxOptions>
              </div>
            </Listbox>
          </div>
          <button type="submit" class="w-full px-4 py-2 bg-button-main text-font-main font-semibold rounded-lg hover:bg-button-mainhover transition duration-300">Зарегистрироваться</button>
        </form>
      </div>
    </div>
    <Footer />
  </div>
</template>
