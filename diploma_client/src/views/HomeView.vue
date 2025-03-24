<script setup lang="ts">
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background-two">
    <NavBar />
    <main class="flex-grow">
      <div class="relative py-16 bg-background-one overflow-hidden">
        <div class="absolute inset-0 pattern-dots-lg text-button-main/10 opacity-60"></div>
        <div class="container mx-auto px-4 text-center relative">
          <h1 class="mb-8 text-8xl md:text-9xl font-great text-font-colored transform hover:scale-105 transition duration-500">
            Lexify
          </h1>
          <p class="mb-4 text-2xl font-main text-font-main max-w-2xl mx-auto leading-relaxed">
            Откройте для себя богатство языков коренных народов России через цифровое погружение
          </p>
          <div class="animate-bounce mt-16">
            <svg class="w-12 h-12 mx-auto text-button-main" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="container mx-auto px-4 py-16">
        <h2 class="font-main text-4xl font-bold text-font-main text-center mb-8 relative">
          <span class="absolute bottom-0 left-1/2 transform -translate-x-1/2 w-32 h-1 bg-button-main"></span>
          Почему стоит выбрать нас
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="bg-background-three p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 group relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-button-main/10 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
            <div class="text-button-main mb-6">
              <svg class="w-16 h-16 mx-auto transform group-hover:rotate-12 transition duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"/>
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Уникальные материалы</h3>
            <p class="text-font-main text-center text-xl mb-4">
              Архивы с редкими учебными материалами, книгами, самоучителями, text-to-speech модели
            </p>
            <div class="text-center">
              <span class="inline-block bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">+1500 документов</span>
            </div>
          </div>

          <div class="bg-background-three p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 group relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-button-main/10 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
            <div class="text-button-main mb-6">
              <svg class="w-16 h-16 mx-auto transform group-hover:rotate-12 transition duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25"/>
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Умный словарь</h3>
            <p class="text-font-main text-center text-xl mb-4">
              Озвучка слов, интегрированный разговорник и система персональных коллекций
            </p>
            <div class="text-center">
              <span class="inline-block bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">+1000 самых популярных слов</span>
            </div>
          </div>

          <div class="bg-background-three p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 group relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-button-main/10 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
            <div class="text-button-main mb-6">
              <svg class="w-16 h-16 mx-auto transform group-hover:rotate-12 transition duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/>
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Билингва-библиотека</h3>
            <p class="text-font-main text-center text-xl mb-4">
              Литература на двух языках с синхронизированным переводом и аудиоверсиями
            </p>
            <div class="text-center">
              <span class="inline-block bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">+200 произведений</span>
            </div>
          </div>
        </div>
      </div>

      <div class="relative py-16 bg-background-one overflow-hidden">
        <div class="absolute inset-0 pattern-dots-lg text-button-main/10 opacity-60"></div>
        <div class="container mx-auto px-4 text-center relative">
          <h1 class="mb-4 text-4xl md:text-6xl font-great text-font-colored transform hover:scale-105 transition duration-500">
            Мост между поколениями
          </h1>
          <p class="mb-4 text-xl font-main text-font-main max-w-3xl mx-auto leading-relaxed">
            Цифровой архив исчезающих языков, сочетающий искусственный интеллект с традиционными знаниями
            носителей для сохранения лингвистического разнообразия России
          </p>
        </div>
      </div>

      <div class="container mx-auto px-4 py-16">
        <div class="max-w-7xl mx-auto">
          <div class="lg:flex gap-12 items-center">
            <div class="lg:w-1/2 mb-12 lg:mb-0">
              <h2 class="text-4xl font-bold text-font-main mb-8 font-main relative">
                <span class="absolute -left-8 top-3 text-button-main text-6xl opacity-30">“</span>
                Лингвистическое наследие в цифровую эпоху
              </h2>
              <p class="text-lg text-font-main font-main mb-6 leading-relaxed">
                Каждые 2 недели в мире исчезает 1 язык. Наша цель - предотвратить эту тенденцию
                для 45 языков народов России, находящихся под угрозой исчезновения.
              </p>
              <div class="bg-background-three p-6 rounded-xl border-l-4 border-button-main">
                <p class="font-main text-font-main">
                  <span class="text-2xl font-bold text-button-main">87%</span><br>
                  языков коренных народов не имеют цифровой поддержки
                </p>
              </div>
            </div>
            <div class="lg:w-1/2 grid gap-6 grid-cols-2">
              <div class="bg-background-three p-6 rounded-xl hover:transform hover:-translate-y-2 transition duration-300">
                <div class="text-5xl font-bold text-button-main mb-4">10+</div>
                <p class="font-main text-font-main">Языков уже доступно</p>
              </div>
              <div class="bg-background-three p-6 rounded-xl hover:transform hover:-translate-y-2 transition duration-300">
                <div class="text-5xl font-bold text-button-main mb-4">2300+</div>
                <p class="font-main text-font-main">Носителей вовлечено</p>
              </div>
              <div class="bg-background-three p-6 rounded-xl hover:transform hover:-translate-y-2 transition duration-300">
                <div class="text-5xl font-bold text-button-main mb-4">20k+</div>
                <p class="font-main text-font-main">Аудиозаписей сгенерировано</p>
              </div>
              <div class="bg-background-three p-6 rounded-xl hover:transform hover:-translate-y-2 transition duration-300">
                <div class="text-5xl font-bold text-button-main mb-4">100+</div>
                <p class="font-main text-font-main">Литературных произведений</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="relative py-12 bg-background-one overflow-hidden">
        <div class="absolute inset-0 pattern-dots-lg text-button-main/10 opacity-60"></div>
        <div class="container mx-auto px-4">
          <h2 class="text-4xl font-bold text-font-main text-center mb-14 font-main relative">
            <span class="absolute bottom-0 left-1/2 transform -translate-x-1/2 w-48 h-1 bg-button-main"></span>
            Поддерживаемые языки
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Татарский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                6+ миллионов носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Учебники</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                50+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Башкирский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                2+ миллионов носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Учебники</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                40+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Чеченский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                1+ миллионов носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Учебники</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                50+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Аварский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                1+ миллионов носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                30+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Лезгинский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                600+ тысяч носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Учебники</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                50+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Якутский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                500+ тысяч носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Учебники</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                30+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Чувашский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                1+ миллионов носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                30+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Осетинский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                700+ тысяч носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                40+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Кумыкский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                500+ тысяч носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                50+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Даргинский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                700+ тысяч носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                30+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Карачаево-Балкарский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                200+ тысяч носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                20+ материалов доступно
              </div>
            </div>

            <div class="bg-background-two p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-button-main/5 to-transparent opacity-0 group-hover:opacity-100 transition duration-500"></div>
              <h3 class="text-2xl font-bold text-font-colored text-center mb-4">Удмуртский</h3>
              <p class="text-font-main text-center text-xl mb-4">
                400+ тысяч носителей
              </p>
              <div class="flex flex-wrap justify-center gap-2">
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Словарь</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Разговорник</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">TTS модель</span>
                <span class="bg-button-main/10 text-button-main px-3 py-1 rounded-full text-sm">Книги</span>
              </div>
              <div class="mt-4 text-center text-sm text-font-main opacity-80">
                20+ материалов доступно
              </div>
            </div>
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
