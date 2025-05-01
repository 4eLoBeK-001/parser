# Агрегатор новостей (Django + Celery + Redis + PostgreSQL)

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

Агрегатор новостей с парсингом из различных источников, системой рейтинга и комментариев.

## Содержание
- [Особенности](#🌟-особенности)
- [Основные библиотеки](#основные-библиотеки)
- [Возможные требования](#возможные-требования)
- [Установка](#установка)
- [Если ошибка с контейнером приложения](#если-ошибка-при-запуске-docker-compose)

## 🌟 Особенности

- Парсинг новостей с Habr и VC.ru
- Система голосования (лайки/дизлайки)
- Комментарии к статьям
- Статистика просмотров
- Периодические задачи (Celery Beat)
- Кеширование (Redis)
- Docker-контейнеризация


## Основные библиотеки
- Django==5.2
- psycopg2-binary==2.9.10
- redis==5.3.0
- celery==5.5.2


## Возможные требования
 - Docker 22.10+
 - Docker Compose version 2.1+

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/4eLoBeK-001/parser.git
    ```

2. Пройдите глубже в проект
    ```
    cd parser
    cd data_aggregator
    ```

3. Запуск проекта
    ```
    docker compose up -d --build
    ```

## Если ошибка при запуске docker compose
Может быть такое, что приложение не смогло подключиться к БД, так как БД запустилось, но не успело настроиться. В связи с чем контейнер приложения может завершиться. В таком случае просто заного запустите контейнер с приложением через `docker start data_aggregator-web-1`