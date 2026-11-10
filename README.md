![CI](https://github.com/redsea1970/cli-scraper/actions/workflows/ci.yml/badge.svg)
# CLI Scraper + CI/CD

Консольная утилита для парсинга HTML-заголовков с сайтов, написанная на Python.

## 🚀 Возможности
- Парсинг заголовков (h1-h6) с любой веб-страницы.
- Сохранение результатов в файл.
- Покрытие тестами (pytest).
- Автоматический запуск тестов через GitHub Actions (CI).

## 🛠 Технологии
- Python 3.12
- BeautifulSoup4, Requests (парсинг)
- Pytest (тестирование)
- Docker & Docker Compose (контейнеризация)
- GitHub Actions (CI/CD)

## 📦 Установка и запуск
```bash
# Клонировать репозиторий
git clone https://github.com/redsea1970/cli-scraper.git

# Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac

# Установить зависимости
pip install -r requirements.txt

# Запустить парсер
python src/scraper.py

## ✅ Локальная проверка (как в CI)
```bash
pip install pytest ruff
ruff check .
pytest tests/ -v
```

## 🔁 CI/CD
При каждом push/PR в `main` GitHub Actions выполняет:
1. **lint** — `ruff check .`
2. **test** — `pytest tests/ -v` (3 теста на `parse_headings`)

Job `test` запускается только после успешного `lint` (`needs: lint`).

## 🐳 Docker
```bash
docker compose up --build
```
