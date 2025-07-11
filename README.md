# Lexify 🌍

**Lexify** — это инновационное приложение для изучения языков малых народов России. Мы помогаем сохранить и популяризировать языковое наследие, предоставляя удобные инструменты для изучения таких языков, как:

- Татарский
- Башкирский
- Чеченский
- Лезгинский
- Якутский

С Lexify вы сможете не только изучать языки, но и погрузиться в культуру малых народов через словари, книги и аудиоматериалы.

---

## ✨ Основные функции

### 📖 **Словарь с переводами и озвучкой**
- Переводчик с русского на выбранный язык.
- Озвучка слов носителями языка для правильного произношения.
- Удобный поиск и категории слов.

### 📚 **Книги с билингва-переводом**
- Литература на двух языках: русском и выбранном.
- Озвучка текстов для улучшения восприятия на слух.
- Возможность читать и слушать одновременно.

### 🗂 **Коллекции слов**
- Создавайте свои коллекции слов для изучения.
- Добавляйте слова из словаря или книг.
- Учите слова с помощью встроенных упражнений.

### 🎧 **Аудиоматериалы**
- Озвучка слов и текстов носителями языка.
- Возможность прослушивания в фоновом режиме.

---

## 🚀 Как начать?

1. **Зарегистрируйтесь** в приложении, выбрав язык для изучения.
2. **Исследуйте словарь** — находите новые слова, слушайте их произношение и добавляйте в коллекции.
3. **Читайте книги** — погружайтесь в мир литературы с билингва-переводом и озвучкой.
4. **Создавайте коллекции** — собирайте слова для заучивания и тренируйтесь.
5. **Следите за прогрессом** — улучшайте свои навыки и достигайте новых уровней.

---

## 🛠 Технологии

- **Frontend**: Vue.js, Pinia, Tailwind CSS
- **Backend**: Django, Django REST Framework
- **База данных**: PostgreSQL
- **Аутентификация**: JWT (JSON Web Tokens)

## 🏗 Архитектура бэкенда

### Основной стек
- **Django 5.1.7** - мощный Python-фреймворк для веб-разработки
- **Django REST Framework 3.15.2** - инструмент для создания RESTful API
- **PostgreSQL** - реляционная база данных
- **Gunicorn** - WSGI HTTP сервер для развертывания

### Аутентификация и безопасность
- **Django REST Framework SimpleJWT** - реализация JWT аутентификации
- **Django CORS Headers** - обработка CORS запросов
- **Django Filter** - фильтрация данных в API

### ML и TTS компоненты
- **PyTorch 2.6.0** - фреймворк для машинного обучения
- **Transformers 4.49.0** - библиотека для работы с NLP моделями
- **HuggingFace Hub** - интеграция с моделями HuggingFace
- **Gradio Client** - взаимодействие с ML моделями

### Дополнительные инструменты
- **Whitenoise** - обработка статических файлов
- **Pillow** - обработка изображений
- **Psycopg2** - PostgreSQL адаптер для Python
- **Websockets** - поддержка веб-сокетов

### Структура проекта
```
diploma_server/
├── apps/                    # Django приложения
│   ├── alphabet/           # Работа с алфавитом
│   ├── dictionary/         # Словарь и переводы
│   ├── library/            # Библиотека книг
│   ├── sources/            # Учебные материалы
│   ├── tts/                # Text-to-Speech система
│   └── users/              # Управление пользователями
├── diploma_server/         # Основные настройки проекта
│   ├── settings.py        # Конфигурация
│   ├── urls.py           # Маршрутизация
│   └── wsgi.py           # WSGI конфигурация
├── staticfiles/           # Статические файлы
└── requirements.txt       # Зависимости проекта
```

### Ключевые особенности
1. **Модульная архитектура** - разделение на независимые приложения
2. **RESTful API** - четкая структура эндпоинтов
3. **JWT аутентификация** - безопасный механизм авторизации
4. **ML интеграция** - использование современных NLP моделей
5. **Асинхронная обработка** - поддержка веб-сокетов для реального времени
6. **Масштабируемость** - возможность горизонтального масштабирования

### Развертывание
- **Gunicorn** для обработки запросов
- **Whitenoise** для статических файлов
- **PostgreSQL** для хранения данных
- **Docker** для контейнеризации (опционально)

## 🧩 Диаграмма компонентов

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|   Vue.js         |     |   Django REST    |     |   PostgreSQL     |
|   Frontend       |     |   Framework      |     |   Database       |
|                  |     |                  |     |                  |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         | HTTP/HTTPS             | ORM                    |
         v                        v                        v
+--------+---------+     +--------+---------+     +--------+---------+
|                  |     |                  |     |                  |
|   Pinia Store    |<--->|   Django         |<--->|   Models         |
|   (State)        |     |   Applications   |     |   (Data)         |
|                  |     |                  |     |                  |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         |                        |                        |
         v                        v                        v
+--------+---------+     +--------+---------+     +--------+---------+
|                  |     |                  |     |                  |
|   Components     |     |   Services       |     |   TTS Engine     |
|   (UI)           |     |   (Business      |     |   (ML Models)    |
|                  |     |   Logic)         |     |                  |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         |                        |                        |
         v                        v                        v
+--------+---------+     +--------+---------+     +--------+---------+
|                  |     |                  |     |                  |
|   Tailwind CSS   |     |   Authentication |     |   File Storage   |
|   (Styling)      |     |   (JWT)          |     |   (Static)       |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
```

### Описание компонентов

1. **Frontend Layer**
   - **Vue.js** - основной фреймворк для UI
   - **Pinia Store** - управление состоянием приложения
   - **Components** - переиспользуемые UI компоненты
   - **Tailwind CSS** - стилизация интерфейса

2. **Backend Layer**
   - **Django REST Framework** - API слой
   - **Django Applications** - бизнес-логика
   - **Authentication** - JWT аутентификация
   - **Services** - сервисный слой

3. **Data Layer**
   - **PostgreSQL** - основное хранилище данных
   - **Models** - ORM модели Django
   - **File Storage** - хранение статических файлов

4. **ML Layer**
   - **TTS Engine** - система синтеза речи
   - **ML Models** - нейронные сети для NLP

### Взаимодействие компонентов

1. **Frontend-Backend**
   - HTTP/HTTPS запросы к API
   - JWT аутентификация
   - WebSocket соединения для реального времени

2. **Backend-Data**
   - ORM взаимодействие с базой данных
   - Миграции и схемы данных
   - Кэширование и оптимизация запросов

3. **Backend-ML**
   - Асинхронная обработка TTS запросов
   - Интеграция с HuggingFace моделями
   - Управление ML пайплайнами

4. **Frontend-ML**
   - Стриминг аудио
   - Интерактивное взаимодействие с TTS
   - Отображение результатов ML

## 📊 Диаграмма вариантов использования

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|   Пользователь   |     |   Администратор  |     |   Система TTS    |
|                  |     |                  |     |                  |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         |                        |                        |
         v                        v                        v
+--------+---------+     +--------+---------+     +--------+---------+
|                  |     |                  |     |                  |
|  Регистрация     |     |  Управление      |     |  Генерация       |
|  и вход          |     |  контентом       |     |  озвучки         |
|                  |     |                  |     |                  |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         |                        |                        |
         v                        v                        v
+--------+---------+     +--------+---------+     +--------+---------+
|                  |     |                  |     |                  |
|  Изучение        |     |  Модерация       |     |  Воспроизведение |
|  алфавита        |     |  материалов      |     |  аудио           |
|                  |     |                  |     |                  |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         |                        |                        |
         v                        v                        v
+--------+---------+     +--------+---------+     +--------+---------+
|                  |     |                  |     |                  |
|  Работа со       |     |  Аналитика       |     |  Синхронизация   |
|  словарем        |     |  использования   |     |  с контентом     |
|                  |     |                  |     |                  |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         |                        |                        |
         v                        v                        v
+--------+---------+     +--------+---------+     +--------+---------+
|                  |     |                  |     |                  |
|  Чтение          |     |  Обновление      |     |  Управление      |
|  билингва-книг   |     |  материалов      |     |  коллекциями     |
|                  |     |                  |     |                  |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         |                        |                        |
         v                        v                        v
+--------+---------+     +--------+---------+     +--------+---------+
|                  |     |                  |     |                  |
|  Тестирование    |     |  Настройка       |     |  Отслеживание    |
|  знаний          |     |  системы         |     |  прогресса       |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
```

### Описание основных вариантов использования:

1. **Пользователь**
   - Регистрация и вход в систему
   - Изучение алфавита выбранного языка
   - Работа со словарем (поиск, добавление в избранное)
   - Чтение билингва-книг
   - Тестирование знаний
   - Управление личными коллекциями слов
   - Отслеживание прогресса обучения

2. **Администратор**
   - Управление контентом (добавление/редактирование материалов)
   - Модерация пользовательского контента
   - Аналитика использования системы
   - Обновление учебных материалов
   - Настройка системы

3. **Система TTS**
   - Генерация озвучки текста
   - Воспроизведение аудио материалов
   - Синхронизация с контентом
   - Управление коллекциями аудио
   - Отслеживание прогресса обучения