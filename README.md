# YaTube API

## Описание

Сам YaTube представляет собой проект социальной сети, в которой реализованы следующие возможности:
публикация записей, комментирование записей, а так же подписки на авторов.
API Yatube - это проект, в котором реализован REST API для проекта Yatube.
Аутентификация настроена на базе Django Rest Framework Simple JWT

## Технологии

- Python 3.7
- Django 2.2.16
- DRF 3.12.4
- Djoser 2.1.0

## Запуск проекта в dev-режиме

- Клонирование репозитория в командной строке

`git clone https://github.com/Stepan-Solnyshkin/api_final_yatube.git`

- Установка и актививация виртуального окружения

`python -3.7 -m venv venv`

`venv/Scripts/activate`

- Уcтановка зависимостей

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

- Запуск сервиса

`python manage.py runserver`

- После запуска сервера полная документация API доступна по адресу:

`http://127.0.0.1:8000/redoc/`

- Получение токена для аутентификации перед началом работы с сервисом

`http://127.0.0.1:8000/api/v1/jwt/create/`

### Автор

Солнышкин Степан

[Обратная связь](https://t.me/nypnyps)
