# YandexDjango
Инструкция для запуска в dev-режиме

## Installing
1. Склонировать репозиторий в папку: git clone ```"https://github.com/Dimmension/yandex_django.git"```
2. Установить зависимости ```"pip install -r /path/to/main_requirements.txt"```,```"pip install -r /path/to/dev_requirements.txt"```,```"pip install -r /path/to/test_requirements.txt"```
3. Создать файл ```".env"```
4. Установить необходимые параметры: ```"SECRET_KEY | DEBUG | ALLOWED_HOSTS"```
5. Запустить сервер ```"python3 manage.py runserver"```