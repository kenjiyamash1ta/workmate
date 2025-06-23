## Описание

Программа для обработки CSV-файлов с поддержкой фильтрации и агрегации данных через командную строку.

## Структура проекта

- `main.py` — основной исполняемый файл
- `core/` — бизнес-логика (чтение, фильтрация, агрегация)
- `cli/` — парсер аргументов командной строки
- `tests/` — модульные тесты

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/kenjiyamash1ta/workmate.git
    cd workmate
    ```

2. Создание виртуального окружения
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```
2. Установите зависимости:
    ```sh
    pip install -r requarement.txt
    ```

## Использование

Примеры запуска:

Без сортировки:
```sh
python main.py --file products.csv --where "price>500" --aggregate "price=avg"
python main.py --file products.csv --where "price<=500" --aggregate "price=max"
python main.py --file products.csv --where "price>=500"
python main.py --file products.csv --aggregate "rating=avg"
python main.py --file products.csv
```

С сортировкой:
```sh
python main.py --file products.csv --order-by "brand=asc"
python main.py --file products.csv --where "price>500" --order-by "price=desc"
python main.py --file products.csv --aggregate "rating=avg" --order-by "name=asc"
python main.py --file products.csv --where "price<=500" --aggregate "price=max" --order-by "price=asc"
```
- `--file` — путь к CSV-файлу (обязательный параметр)
- `--where` — фильтр (например, `"price>500"`)
- `--aggregate` — агрегация (например, `"price=avg"`)
- `--order-by` — сортировка по колонке, например `"brand=asc"` или `"price=desc"`

## Тестирование

Для запуска всех тестов:
```sh
pytest
```

## Проверка покрытия тестами

Для запуска тестов с анализом покрытия:
```sh
pytest --cov=core --cov=cli --cov-report=term-missing tests/
```

---
