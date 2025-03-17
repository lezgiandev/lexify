import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import { useAuthStore } from '@/stores/authStore';
import DictionaryView from "@/views/DictionaryView.vue";
import LibraryView from "@/views/LibraryView.vue";
import BookView from "@/views/BookView.vue";
import ProfileView from "@/views/ProfileView.vue";
import SourceView from "@/views/SourceView.vue";
import AlphabetView from "@/views/AlphabetView.vue";
import TTSView from "@/views/TTSView.vue";


const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomeView },
    { path: '/alphabet', component: AlphabetView, meta: { requiresAuth: true } },
    { path: '/tts', component: TTSView, meta: { requiresAuth: true } },
    { path: '/dictionary', component: DictionaryView, meta: { requiresAuth: true } },
    { path: '/library', component: LibraryView, meta: { requiresAuth: true } },
    { path: '/sources', component: SourceView, meta: { requiresAuth: true } },
    { path: '/profile', component: ProfileView, meta: { requiresAuth: true } },
    { path: '/library/:bookId', component: BookView, meta: { requiresAuth: true }, name: 'book' },
    { path: '/login', component: LoginView },
    { path: '/register', component: RegisterView },
  ],
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;
