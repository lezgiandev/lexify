<template>
  <footer class="bg-darktwo text-goldlight font-semibold">
    <div class="container mx-auto px-4 py-8">
      <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8">
        <div>
          <h3 class="text-lg font-bold mb-4 font-main">О нас</h3>
          <p class="text-light/70 font-main">
            Lexify — это платформа для изучения языков коренных народов России, которая помогает вам улучшать свои навыки с помощью словарей, коллекций и нашей уникальной библиотеки.
          </p>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 font-main">Быстрые ссылки</h3>
          <ul class="space-y-2">
            <li><router-link to="/alphabet" class="text-light/70 hover:text-golddark transition duration-300 font-main">Алфавит</router-link></li>
            <li><router-link to="/tts" class="text-light/70 hover:text-golddark transition duration-300 font-main">Озвучка</router-link></li>
            <li><router-link to="/dictionary" class="text-light/70 hover:text-golddark transition duration-300 font-main">Словарь</router-link></li>
            <li><router-link to="/library" class="text-light/70 hover:text-golddark transition duration-300 font-main">Библиотека</router-link></li>
            <li><router-link to="/sources" class="text-light/70 hover:text-golddark transition duration-300 font-main">Источники</router-link></li>
            <li><router-link to="/settings" class="text-light/70 hover:text-golddark transition duration-300 font-main">Настройки</router-link></li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 font-main">Контакты</h3>
          <ul class="space-y-2">
            <li class="text-light/70 font-main">Email: lexify.study@gmail.com</li>
            <li class="text-light/70 font-main">Телефон: +1 (999) 999-99-99</li>
            <li class="text-light/70 font-main">Адрес: ЯГТУ, ул. Дипломная, 1</li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 font-main">Социальные сети</h3>
          <ul class="space-y-2">
            <li class="text-light/70 font-main hover:text-golddark transition duration-300">
              <a href="#">
                GitGub
              </a>
            </li>
            <li class="text-light/70 font-main hover:text-golddark transition duration-300">
              <a href="#">
                Telegram
              </a>
            </li>
            <li class="text-light/70 font-main hover:text-golddark transition duration-300">
              <a href="#">
                ВКонтакте
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div class="border-t text-light/70 mt-8 pt-8 text-center font-main">
        <p class="text-light/70">&copy; 2025 Lexify. Все права защищены.</p>
      </div>
    </div>
  </footer>
</template>
<script setup lang="ts">
</script>
