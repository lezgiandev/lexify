<template>
  <footer class="bg-footer-main text-footer-heading">
    <div class="container mx-auto px-4 py-8">
      <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8">
        <div>
          <h3 class="text-lg font-bold mb-4 font-main">О нас</h3>
          <p class="text-footer-content font-main">
            Lexify — это платформа для изучения языков коренных народов России, которая помогает вам улучшать свои навыки с помощью словарей, коллекций и нашей уникальной библиотеки.
          </p>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 font-main">Быстрые ссылки</h3>
          <ul class="space-y-2">
            <li><router-link to="/alphabet" class="text-footer-content hover:text-footer-hover transition duration-300 font-main">Алфавит</router-link></li>
            <li><router-link to="/tts" class="text-footer-content hover:text-footer-hover transition duration-300 font-main">Озвучка</router-link></li>
            <li><router-link to="/dictionary" class="text-footer-content hover:text-footer-hover transition duration-300 font-main">Словарь</router-link></li>
            <li><router-link to="/library" class="text-footer-content hover:text-footer-hover transition duration-300 font-main">Библиотека</router-link></li>
            <li><router-link to="/sources" class="text-footer-content hover:text-footer-hover transition duration-300 font-main">Источники</router-link></li>
            <li><router-link to="/settings" class="text-footer-content hover:text-footer-hover transition duration-300 font-main">Настройки</router-link></li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 font-main">Контакты</h3>
          <ul class="space-y-2">
            <li class="text-footer-content font-main">Email: lexify.study@gmail.com</li>
            <li class="text-footer-content font-main">Телефон: +7 (960) 543-01-96</li>
            <li class="text-footer-content font-main">Адрес: Ярославль, ул. Труфанова, 34а</li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 font-main">Социальные сети</h3>
          <div class="flex space-x-4">
            <!-- GitHub -->
            <a href="#" class="text-footer-content hover:text-footer-hover transition duration-300">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.098 2.65.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
              </svg>
            </a>

            <!-- Telegram -->
            <a href="#" class="text-footer-content hover:text-footer-hover transition duration-300">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm5.894 8.221l-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.446 1.394c-.14.14-.26.26-.51.26l.213-3.053 5.56-5.022c.24-.213-.054-.334-.373-.121l-6.87 4.326-2.962-.924c-.64-.203-.658-.64.135-.954l11.566-4.458c.538-.196 1.006.128.832.941z" />
              </svg>
            </a>
          </div>
        </div>
      </div>

      <div class="border-t border-footer-border mt-8 pt-8 text-center font-main">
        <p class="text-footer-heading">&copy; 2025 Lexify. Все права защищены.</p>
      </div>
    </div>
  </footer>
</template>
<script setup lang="ts">
</script>
