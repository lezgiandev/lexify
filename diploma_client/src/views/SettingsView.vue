<script setup lang="ts">
import NavBar from "@/components/NavBar.vue";
import { useUserStore } from "@/stores/userStore.ts";
import Footer from "@/components/Footer.vue";
import { onMounted, ref } from "vue";
import { useAuthStore } from '@/stores/authStore';
import CustomListbox from "@/components/CustomListbox.vue";
import PasswordInput from "@/components/PasswordInput.vue";

const authStore = useAuthStore();
const userStore = useUserStore();

const selectedLanguageId = ref<number | null>(null);
const oldPassword = ref('');
const newPassword = ref('');
const confirmPassword = ref('');
const message = ref('');
const error = ref('');

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
  <div class="min-h-screen flex flex-col bg-darkone">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8 max-w-2xl">
      <div class="mb-8 relative">
        <h1 class="text-light text-3xl font-bold font-main">
          Настройки
          <span class="absolute bottom-0 left-0 w-24 h-1 bg-goldlight mt-2"></span>
        </h1>
      </div>

      <div class="mb-6 font-main">
        <h2 class="text-light text-xl font-semibold mb-4">Изучаемый язык</h2>
        <CustomListbox
          v-model="selectedLanguageId"
          :options="userStore.languages"
          default-label="Выберите язык"
        />
        <div class="flex items-center gap-4 mt-6">
          <button
            @click="handleLanguageUpdate"
            class="px-4 py-2 bg-goldlight text-darkone rounded-xl font-semibold  hover:bg-golddark transition duration-300"
          >
            Сохранить язык
          </button>
          <span v-if="userStore.language" class="text-light">
            Текущий язык: {{ userStore.language.name }}
          </span>
        </div>
      </div>

      <div class="mb-6 font-main">
        <h2 class="text-light text-xl font-semibold mb-6">Смена пароля</h2>
        <form @submit.prevent="handleChangePassword" class="space-y-6">
          <PasswordInput
            v-model="oldPassword"
            placeholder="Старый пароль"
            required
          />

          <PasswordInput
            v-model="newPassword"
            placeholder="Новый пароль"
            required
          />

          <PasswordInput
            v-model="confirmPassword"
            placeholder="Подтвердите пароль"
            required
          />

          <button
            type="submit"
            class="px-4 py-2 bg-goldlight text-darkone rounded-xl font-semibold hover:bg-golddark transition duration-300"
          >
            Сменить пароль
          </button>
        </form>
      </div>

      <div v-if="message" class="p-4 mb-4 bg-light text-greenlight rounded-xl">
        {{ message }}
      </div>
      <div v-if="error" class="p-4 mb-4 bg-light text-redlight rounded-xl">
        {{ error }}
      </div>

      <button
        @click="authStore.logout"
        class="p-4 font-main bg-redlight text-darkone rounded-xl font-bold shadow-lg hover:shadow-xl hover:bg-reddark transition-all duration-300 flex items-center justify-center"
      >
        Выйти из аккаунта
      </button>
    </main>
    <Footer />
  </div>
</template>
