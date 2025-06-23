# workmate

Тестовое задание для стажировки.

## Описание

Программа для обработки CSV-файлов с поддержкой фильтрации и агрегации данных через командную строку.

## Структура проекта

- `main.py` — основной исполняемый файл
- `core/` — бизнес-логика (чтение, фильтрация, агрегация)
- `cli/` — парсер аргументов командной строки
- `tests/` — модульные тесты

## Требования

- Python 3.10+
- Зависимости из файла [requarement.txt](requarement.txt)

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone git@github.com:kenjiyamash1ta/workmate.git
    cd workmate
    ```

2. Создание виртуального окружения
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\\Scripts\\activate  # Windows
    ```
2. Установите зависимости:
    ```sh
    pip install -r requarement.txt
    ```

## Использование

Пример запуска:
```sh
python main.py --file products.csv --where "price>500" --aggregate "price=avg"
```
- `--file` — путь к CSV-файлу (обязательный параметр)
- `--where` — фильтр (например, `"price>500"`)
- `--aggregate` — агрегация (например, `"price=avg"`)

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

Покрытие будет выведено в консоль.  
Файл `.coverage` содержит подробную информацию для инструментов анализа покрытия.

---