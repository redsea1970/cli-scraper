# Архитектура проекта

## Компоненты

```mermaid
flowchart TD
    U[Пользователь] --> A[CLI / argparse]
    A --> B[Скрапер]
    B --> C[requests + BeautifulSoup]
    B --> D[SQLite]
    C --> B
    D --> B
    B --> A
    A --> U
