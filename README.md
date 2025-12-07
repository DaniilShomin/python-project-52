### Hexlet tests and linter status:
[![Actions Status](https://github.com/DaniilShomin/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DaniilShomin/python-project-52/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DaniilShomin_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DaniilShomin_python-project-52)
[![Python CI](https://github.com/DaniilShomin/python-project-52/actions/workflows/pyci.yml/badge.svg)](https://github.com/DaniilShomin/python-project-52/actions/workflows/pyci.yml)

# Task Manager 🎯

**Демо:** [https://python-project-52-zib0.onrender.com](https://python-project-52-zib0.onrender.com)

## Быстрый старт ⚡

### Установка
```bash
# 1. Клонировать репозиторий
git clone https://github.com/DaniilShomin/python-project-52.git
cd python-project-52

# 2. Настроить окружение
cp .env.example .env  # отредактируйте .env

# 3. Установить зависимости
make install
make migrate
```

### Запуск
```bash
# Разработка
make start-server

# Доступно по адресу: http://localhost:8000
```

## Особенности ✨

- 🔐 **Регистрация и авторизация** пользователей
- ✅ **Управление задачами** (CRUD)
- 🏷️ **Метки и статусы** для задач
- 🔍 **Фильтрация** по меткам, исполнителю, статусу
- 📱 **Адаптивный дизайн** (Bootstrap 5)

## Технологии 🛠️

- Python 3.10+
- Django 4.2+
- PostgreSQL / SQLite
- Bootstrap 5
- Gunicorn

## Основные команды 🔧

```bash
make install      # Установить зависимости
make start-server # Запустить сервер
make test         # Запустить тесты
make lint         # Проверить код
make migrate      # Применить миграции
```
