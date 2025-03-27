<template>
  <footer class="bg-zinc-800 text-white font-semibold">
    <div class="container mx-auto px-4 py-8">
      <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8">
        <div>
          <h3 class="text-lg font-bold mb-4 font-main">О нас</h3>
          <p class="text-zinc-300 font-main">
            Lexify — это платформа для изучения языков коренных народов России, которая помогает вам улучшать свои навыки с помощью словарей, коллекций и нашей уникальной библиотеки.
          </p>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 font-main">Быстрые ссылки</h3>
          <ul class="space-y-2">
            <li><router-link to="/alphabet" class="text-zinc-300 hover:text-violet-500 transition duration-300 font-main">Алфавит</router-link></li>
            <li><router-link to="/tts" class="text-zinc-300 hover:text-violet-500 transition duration-300 font-main">Озвучка</router-link></li>
            <li><router-link to="/dictionary" class="text-zinc-300 hover:text-violet-500 transition duration-300 font-main">Словарь</router-link></li>
            <li><router-link to="/library" class="text-zinc-300 hover:text-violet-500 transition duration-300 font-main">Библиотека</router-link></li>
            <li><router-link to="/sources" class="text-zinc-300 hover:text-violet-500 transition duration-300 font-main">Источники</router-link></li>
            <li><router-link to="/settings" class="text-zinc-300 hover:text-violet-500 transition duration-300 font-main">Настройки</router-link></li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 font-main">Контакты</h3>
          <ul class="space-y-2">
            <li class="text-zinc-300 font-main">Email: lexify.study@gmail.com</li>
            <li class="text-zinc-300 font-main">Телефон: +7 (960) 543-01-96</li>
            <li class="text-zinc-300 font-main">Адрес: Ярославль, ул. Труфанова, 34а</li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 font-main">Социальные сети</h3>
          <ul class="space-y-2">
            <li class="text-zinc-300 font-main hover:text-violet-500 transition duration-300">
              <a href="#">
                GitGub
              </a>
            </li>
            <li class="text-zinc-300 font-main hover:text-violet-500 transition duration-300">
              <a href="#">
                Telegram
              </a>
            </li>
            <li class="text-zinc-300 font-main hover:text-violet-500 transition duration-300">
              <a href="#">
                ВКонтакте
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div class="border-t border-zinc-100 mt-8 pt-8 text-center font-main">
        <p class="text-zinc-100">&copy; 2025 Lexify. Все права защищены.</p>
      </div>
    </div>
  </footer>
</template>
<script setup lang="ts">
</script>
