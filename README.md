# CLI Scraper

CLI-утилита для парсинга заголовков с сайта и сохранения в SQLite.

## Что делает
- Принимает URL через аргументы командной строки (`argparse`).
- Парсит заголовки (`<h1>`, `<h2>`, `<h3>`) с помощью `requests` + `BeautifulSoup`.
- Сохраняет в SQLite (таблица `headings`).
- Выводит статистику: сколько заголовков каждого уровня.
- Логирует действия в консоль и файл (`logging`).

## Стек
- Python 3.12
- argparse, logging, sqlite3 (встроены)
- requests, beautifulsoup4

## Как запустить
    pip install -r requirements.txt
    python src/scraper.py --url https://example.com --db data/headings.db

## Автор
itpso
