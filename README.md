# LMS-система

LMS-система - это веб-приложение, позволяющее пользователям размещать свои полезные материалы или курсы.

## Описание

LMS-система позволяет создавать и управлять курсами, добавлять материалы, а также предоставляет функционал для управления пользователями и их доступами.

## Требования к проекту

* Python: версия 3.8 или выше
* Django: версия 3.2 или выше
* PostgreSQL: версия 12 или выше


## Инструкции по установке и запуску проекта

1. Клонировать репозиторий: `git clone https://github.com/kuzinnatra/24_1.git`
2. Перейти в папку проекта: `cd project`
3. Установить зависимости: `pip install -r requirements.txt`
4.  Создайте файл `.env` в корневой папке проекта и заполните его по шаблону `.env.sample` переменными:
 * `SECRET_KEY`: секретный ключ проекта (например, случайная строка из 50 символов)
 * `NAME`: имя базы данных
 * `USER`: имя пользователя базы данных
 * `PASSWORD`: пароль пользователя базы данных
 * `HOST`: адрес хоста базы данных (например, localhost)
 * `PORT`: порт базы данных (например, 5432)
5. Создать базу данных: `python manage.py migrate`
6. Запустить сервер: `python manage.py runserver`

