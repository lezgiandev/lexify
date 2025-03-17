import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { loginUser, registerUser } from '@/services/authService';

export const useAuthStore = defineStore('auth', () => {
  const token = ref<string | null>(localStorage.getItem('token'));
  const isAuthenticated = ref<boolean>(!!token.value);
  const router = useRouter();

  const login = async (credentials: {
    username: string;
    password: string
  }) => {
    try {
      const response = await loginUser(credentials);
      token.value = response.access;
      isAuthenticated.value = true;
      localStorage.setItem('token', response.access);
      await router.push('/');
    } catch (error) {
      console.error('Login failed', error);
    }
  };

  const register = async (userData: {
    username: string;
    password: string;
    language: number
  }) => {
    try {
      const response = await registerUser(userData);
      token.value = response.access;
      isAuthenticated.value = true;
      localStorage.setItem('token', response.access);
      await router.push('/');
    } catch (error) {
      console.error('Registration failed', error);
    }
  };

  const logout = async () => {
    token.value = null;
    isAuthenticated.value = false;
    localStorage.removeItem('token');
    try {
      await router.push('/login');
    } catch (error) {
      console.error('Navigation error:', error);
    }
  };

  return {
    token,
    isAuthenticated,
    login,
    register,
    logout
  };
});
