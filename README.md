
# Тестовое задание Тензор

Автоматизированные UI-тесты Яндекс.Картинок и поиска Яндекса.

## Технологии

- Python 3.13
- Selenium 4.52.0
- Pytest 9.2.0
- Page Object Model

## Структура проекта

```text
tenzor_test/
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   ├── search_results_page.py
│   └── images_page.py
├── tests/
│   ├── test_search.py
│   └── test_images.py
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Установка

```bash
git clone https://github.com/Fletcher2250/tenzor_test.git
cd tenzor_test
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск тестов

Все тесты:

```bash
pytest -v
```

Только поиск:

```bash
pytest -v tests/test_search.py
```

Только картинки:

```bash
pytest -v tests/test_images.py
```

## Реализованные проверки

### Поиск Яндекса

- Открытие главной страницы.
- Ввод запроса «Тензор».
- Проверка поисковых подсказок.
- Переход к результатам.
- Проверка ссылки первого найденного не рекламного результата на tensor.ru.

### Яндекс.Картинки

- Открытие страницы картинок.
- Открытие первого изображения.
- Проверка загрузки изображения.
- Переход к следующему изображению.
- Возврат к исходному изображению.

## Результаты

Последний локальный запуск:

- test_search_tensor_is_first_result — PASSED
- test_yandex_images_navigation — PASSED
