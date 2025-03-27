<script setup lang="ts">
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import FeatureCard from '@/components/FeatureCard.vue';
import LanguageCard from '@/components/LanguageCard.vue';
import SectionTitle from '@/components/SectionTitle.vue';

const languages = [
  {
    title: 'Татарский',
    speakers: '6+ миллионов носителей',
    tags: ['Словарь', 'Разговорник', 'TTS модель', 'Учебники', 'Книги'],
    materials: '60+ материалов доступно'
  },
  {
    title: 'Башкирский',
    speakers: '2+ миллионов носителей',
    tags: ['Словарь', 'Разговорник', 'TTS модель', 'Учебники', 'Книги'],
    materials: '40+ материалов доступно'
  },
  {
    title: 'Чеченский',
    speakers: '1+ миллионов носителей',
    tags: ['Словарь', 'Разговорник', 'TTS модель', 'Учебники', 'Книги'],
    materials: '40+ материалов доступно'
  },
  {
    title: 'Якутский',
    speakers: '500+ тысяч носителей',
    tags: ['Словарь', 'Разговорник', 'TTS модель', 'Учебники', 'Книги'],
    materials: '30+ материалов доступно'
  },
  {
    title: 'Аварский',
    speakers: '1+ миллионов носителей',
    tags: ['Словарь', 'Разговорник', 'TTS модель', 'Учебники'],
    materials: '40+ материалов доступно'
  },
  {
    title: 'Лезгинский',
    speakers: '600+ тысяч носителей',
    tags: ['Словарь', 'Разговорник', 'TTS модель', 'Книги'],
    materials: '40+ материалов доступно'
  },
  {
    title: 'Чувашский',
    speakers: '1+ миллионов носителей',
    tags: ['Словарь', 'TTS модель', 'Учебники', 'Книги'],
    materials: '40+ материалов доступно'
  },
  {
    title: 'Осетинский',
    speakers: '700+ тысяч носителей',
    tags: ['Словарь', 'Разговорник', 'TTS модель', 'Книги'],
    materials: '30+ материалов доступно'
  },
];
</script>

<template>
  <div class="min-h-screen flex flex-col bg-zinc-800">
    <NavBar />
    <main class="flex-grow">
      <div class="relative py-16 bg-zinc-900 overflow-hidden">
        <div class="absolute inset-0 pattern-dots-lg text-violet-500/10 opacity-60"></div>
        <div class="container mx-auto px-4 text-center relative">
          <h1 class="mb-8 text-7xl md:text-8xl font-great text-violet-500 transform hover:scale-105 transition duration-500">
            Lexify
          </h1>
          <p class="mb-4 text-2xl font-main text-white max-w-2xl mx-auto leading-relaxed">
            Откройте для себя богатство языков коренных народов России через цифровое погружение
          </p>
          <div class="animate-[bounce_2s_infinite] mt-4">
            <svg class="w-16 h-16 mx-auto drop-shadow-xl" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M26 40L32 45L38 40"
                stroke="url(#grad)"
                stroke-width="5"
                stroke-linecap="round"
                stroke-linejoin="round"
                fill="none"
                style="transform: translateY(5px)"/>

              <defs>
                <linearGradient
                  id="grad"
                  x1="32"
                  y1="40"
                  x2="32"
                  y2="52"
                  gradientUnits="userSpaceOnUse">
                  <stop stop-color="#A78BFA" offset=""/>
                  <stop offset="0.7" stop-color="#8b5cf6"/>
                </linearGradient>
              </defs>
            </svg>
          </div>
        </div>
      </div>

      <div class="container mx-auto px-4 py-8">
        <SectionTitle text="Почему стоит выбрать нас" />
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <FeatureCard
            title="Уникальные материалы"
            description="Архивы с редкими учебными материалами, книгами, самоучителями, text-to-speech модели"
            tag="+1500 документов"
          >
            <template #icon>
              <svg class="w-16 h-16 mx-auto transform group-hover:rotate-12 transition duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"/>
              </svg>
            </template>
          </FeatureCard>

          <FeatureCard
            title="Умный словарь"
            description="Озвучка слов, интегрированный разговорник и система персональных коллекций"
            tag="+1000 самых популярных слов"
          >
            <template #icon>
              <svg class="w-16 h-16 mx-auto transform group-hover:rotate-12 transition duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25"/>
              </svg>
            </template>
          </FeatureCard>

          <FeatureCard
            title="Билингва-библиотека"
            description="Литература на двух языках с синхронизированным переводом и аудиоверсиями"
            tag="+200 произведений"
          >
            <template #icon>
              <svg class="w-16 h-16 mx-auto transform group-hover:rotate-12 transition duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/>
              </svg>
            </template>
          </FeatureCard>
        </div>
      </div>

      <div class="relative py-12 bg-zinc-900 overflow-hidden">
        <div class="absolute inset-0 pattern-dots-lg text-violet-500/10 opacity-60"></div>
        <div class="container mx-auto px-4">
          <SectionTitle text="Поддерживаемые языки" />
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <LanguageCard
              v-for="(language, index) in languages"
              :key="index"
              :title="language.title"
              :speakers="language.speakers"
              :tags="language.tags"
              :materials="language.materials"
            />
          </div>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<style>
.pattern-dots-lg {
  background-image: radial-gradient(currentColor 1px, transparent 1px);
  background-size: calc(20px * 1) calc(20px * 1);
}

@keyframes gradient-wave {
  0% { background-position: 0 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0 50%; }
}

.pattern-dots-lg {
  background-image: radial-gradient(currentColor 1px, transparent 1px);
  background-size: calc(20px * 1) calc(20px * 1);
}

@keyframes gradient-wave {
  0% { background-position: 0 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0 50%; }
}
</style>
