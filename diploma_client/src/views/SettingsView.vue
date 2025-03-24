<script setup lang="ts">
import NavBar from "@/components/NavBar.vue";
import { useUserStore } from "@/stores/userStore.ts";
import Footer from "@/components/Footer.vue";
import { onMounted, ref } from "vue";
import { useAuthStore } from '@/stores/authStore';
import CustomListbox from "@/components/CustomListbox.vue";

const authStore = useAuthStore();
const userStore = useUserStore();

const selectedLanguageId = ref<number | null>(null);
const oldPassword = ref('');
const newPassword = ref('');
const confirmPassword = ref('');
const message = ref('');
const error = ref('');
const showPassword = ref(false);

onMounted(async () => {
  await userStore.fetchUserLanguage();
  await userStore.fetchAllLanguages();
  selectedLanguageId.value = userStore.language?.id || null;
});

const handleLanguageUpdate = async () => {
  error.value = '';
  message.value = '';

  if (newPassword.value !== confirmPassword.value) {
    error.value = 'Пароли не совпадают';
    return;
  }

  if (!selectedLanguageId.value) {
    error.value = 'Пожалуйста, выберите язык';
    return;
  }

  try {
    await userStore.updateLanguage(selectedLanguageId.value);
    message.value = 'Язык успешно изменен!';
  } catch (err) {
    error.value = 'Ошибка при изменении языка';
  }
};

const handleChangePassword = async () => {
  error.value = '';
  message.value = '';

  if (newPassword.value !== confirmPassword.value) {
    error.value = 'Пароли не совпадают';
    return;
  }

  try {
    await userStore.changePassword({
      old_password: oldPassword.value,
      new_password: newPassword.value,
    });

    message.value = 'Пароль успешно изменен!';
    oldPassword.value = '';
    newPassword.value = '';
    confirmPassword.value = '';
  } catch (err) {
    error.value = 'Ошибка при смене пароля';
  }
};
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8 max-w-2xl">
      <div class="mb-8 relative">
        <h1 class="text-font-main text-3xl font-bold font-great">
          Настройки
          <span class="absolute bottom-0 left-0 w-24 h-1 bg-button-main mt-2"></span>
        </h1>
      </div>

      <div class="mb-6 font-main">
        <h2 class="text-font-main text-xl font-semibold mb-4">Язык интерфейса</h2>
        <CustomListbox
          v-model="selectedLanguageId"
          :options="userStore.languages"
          default-label="Выберите язык"
        />
        <div class="flex items-center gap-4 mt-4">
          <button
            @click="handleLanguageUpdate"
            class="px-4 py-2 bg-button-main text-button-text rounded-xl font-semibold  hover:bg-button-mainhover transition duration-300"
          >
            Сохранить язык
          </button>
          <span v-if="userStore.language" class="text-font-main">
            Текущий язык: {{ userStore.language.name }}
          </span>
        </div>
      </div>

      <div class="mb-6 font-main">
        <h2 class="text-font-main text-xl font-semibold mb-6">Смена пароля</h2>
        <form @submit.prevent="handleChangePassword" class="space-y-6">
          <div class="group relative">
            <input
              v-model="oldPassword"
              :type="showPassword ? 'text' : 'password'"
              required
              class="w-full px-6 py-4 bg-background-two rounded-xl text-font-main
                focus:outline-none focus:ring-2 focus:ring-button-main
                border-2 border-transparent focus:border-button-main
                transition-all duration-300 placeholder-transparent pr-12"
              placeholder=" "
            />
            <label class="absolute left-4 top-1 text-sm text-font-main opacity-75
                 group-focus-within:-translate-y-7 group-focus-within:scale-90
                 transition-all duration-300 pointer-events-none">
              Старый пароль
            </label>

            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-4 top-1/2 -translate-y-1/2 text-font-main/50 hover:text-font-main transition-colors"
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

          <div class="group relative">
            <input
              v-model="newPassword"
              :type="showPassword ? 'text' : 'password'"
              required
              class="w-full px-6 py-4 bg-background-two rounded-xl text-font-main
                focus:outline-none focus:ring-2 focus:ring-button-main
                border-2 border-transparent focus:border-button-main
                transition-all duration-300 placeholder-transparent pr-12"
              placeholder=" "
            />
            <label class="absolute left-4 top-1 text-sm text-font-main opacity-75
                 group-focus-within:-translate-y-7 group-focus-within:scale-90
                 transition-all duration-300 pointer-events-none">
              Новый пароль
            </label>

            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-4 top-1/2 -translate-y-1/2 text-font-main/50 hover:text-font-main transition-colors"
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

          <div class="group relative">
            <input
              v-model="confirmPassword"
              :type="showPassword ? 'text' : 'password'"
              required
              class="w-full px-6 py-4 bg-background-two rounded-xl text-font-main
                focus:outline-none focus:ring-2 focus:ring-button-main
                border-2 border-transparent focus:border-button-main
                transition-all duration-300 placeholder-transparent pr-12"
              placeholder=" "
            />
            <label class="absolute left-4 top-1 text-sm text-font-main opacity-75
                 group-focus-within:-translate-y-7 group-focus-within:scale-90
                 transition-all duration-300 pointer-events-none">
              Подтвердите пароль
            </label>

            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-4 top-1/2 -translate-y-1/2 text-font-main/50 hover:text-font-main transition-colors"
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

          <button
            type="submit"
            class="px-4 py-2 bg-button-main text-button-text rounded-xl font-semibold hover:bg-button-mainhover transition duration-300"
          >
            Сменить пароль
          </button>
        </form>
      </div>

      <div v-if="message" class="p-4 mb-4 bg-green-100 text-green-700 rounded-xl">
        {{ message }}
      </div>
      <div v-if="error" class="p-4 mb-4 bg-red-100 text-red-700 rounded-xl">
        {{ error }}
      </div>

      <button
        @click="authStore.logout"
        class="p-4 font-main bg-button-cancel text-button-text rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-button-cancelhover transition-all duration-300 flex items-center justify-center"
      >
        Выйти из аккаунта
      </button>
    </main>
    <Footer />
  </div>
</template>
