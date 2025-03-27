<template>
  <div class="bg-zinc-900">
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '@/stores/authStore';

const authStore = useAuthStore();
authStore.token = localStorage.getItem('token');
authStore.isAuthenticated = !!authStore.token;
</script>
