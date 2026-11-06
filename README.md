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
