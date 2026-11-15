

\# Тестовое задание Тензор



Автоматизированные UI-тесты сайта Яндекс с использованием Python, Selenium WebDriver и Pytest.



\## Требования



\- Python 3.13+

\- Google Chrome

\- Selenium 4.52.0

\- Pytest 9.2.0



\## Структура проекта



```text

tenzor\_test/

│

├── pages/

│   ├── \_\_init\_\_.py

│   ├── base\_page.py

│   ├── main\_page.py

│   ├── search\_results\_page.py

│   └── images\_page.py

│

├── tests/

│   ├── test\_search.py

│   └── test\_images.py

│

├── conftest.py

├── requirements.txt

└── README.md

```



\## Установка



Клонировать репозиторий:



```bash

git clone <ССЫЛКА\_НА\_РЕПОЗИТОРИЙ>

cd tenzor\_test

```



Создать виртуальное окружение:



```bash

python -m venv .venv

```



Активировать его в Windows:



```bash

.venv\\Scripts\\activate

```



Установить зависимости:



```bash

pip install -r requirements.txt

```



\## Запуск тестов



Запустить все тесты:



```bash

pytest -v

```



Запустить только тест поиска:



```bash

pytest -v tests/test\_search.py

```



Запустить только тест Яндекс.Картинок:



```bash

pytest -v tests/test\_images.py

```



\## Реализованные проверки



\### Поиск



\- Открытие главной страницы Яндекса.

\- Ввод поискового запроса «Тензор».

\- Проверка введённого значения.

\- Ожидание появления поисковых подсказок.

\- Переход к результатам поиска.

\- Проверка, что первый найденный не рекламный результат ведёт на `tensor.ru`.



\### Яндекс.Картинки



\- Открытие страницы Яндекс.Картинок.

\- Открытие первого изображения.

\- Проверка загрузки изображения.

\- Переход к следующему изображению.

\- Возврат к предыдущему изображению.

\- Проверка возврата к исходному изображению.



\## Используемые технологии



\- Python

\- Selenium WebDriver

\- Pytest

\- Page Object Model


## Результаты тестирования

Оба автоматизированных теста успешно пройдены:

- `test_search_tensor_is_first_result` — PASSED
- `test_yandex_images_navigation` — PASSED

Запуск выполнен командой `pytest -v`.
