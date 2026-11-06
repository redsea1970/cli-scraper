import argparse
import logging
import sqlite3
import sys
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("scraper.log", encoding="utf-8"),
        ],
    )


def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS headings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            level TEXT NOT NULL,
            text TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def fetch_page(url):
    logging.info(f"Загрузка: {url}")
    headers = {"User-Agent": "Mozilla/5.0 (CLI-Scraper/1.0)"}
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.text


def parse_headings(html):
    soup = BeautifulSoup(html, "html.parser")
    headings = []
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            headings.append((tag.name, text))
    return headings


def save_headings(conn, url, headings):
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO headings (url, level, text) VALUES (?, ?, ?)",
        [(url, level, text) for level, text in headings],
    )
    conn.commit()


def print_stats(headings):
    stats = {"h1": 0, "h2": 0, "h3": 0}
    for level, _ in headings:
        stats[level] += 1
    logging.info("Статистика заголовков:")
    for level, count in stats.items():
        logging.info(f"  {level}: {count}")


def main():
    parser = argparse.ArgumentParser(description="CLI-скрапер заголовков")
    parser.add_argument("--url", required=True, help="URL страницы")
    parser.add_argument("--db", default="data/headings.db", help="Путь к SQLite")
    args = parser.parse_args()

    setup_logging()

    parsed = urlparse(args.url)
    if not parsed.scheme or not parsed.netloc:
        logging.error("Некорректный URL. Пример: https://example.com")
        sys.exit(1)

    try:
        html = fetch_page(args.url)
        headings = parse_headings(html)
        logging.info(f"Найдено заголовков: {len(headings)}")

        conn = init_db(args.db)
        save_headings(conn, args.url, headings)
        conn.close()

        print_stats(headings)
        logging.info(f"Сохранено в БД: {args.db}")
    except requests.RequestException as e:
        logging.error(f"Ошибка сети: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Неожиданная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
