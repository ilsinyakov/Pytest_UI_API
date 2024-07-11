# Pytest_UI_API

## Шаблон для автоматизации тестирования на python

### Шаги

1. Склонировать проект `git clone git@github.com:ilsinyakov/Pytest_UI_API.git`
2. Установить зависимости `pip install -r requirements.txt`
3. Запустить тесты `pytest`
4. Сгенерировать allure-отчет `allure generate allure-files -o allure-report`
5. Открыть allure-отчет `allure open allure-report`

### Стек

- pytest
- selenium
- requests
- *sqlalchemy*
- allure
- config

### Структура

- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- *./db - хелперы для работы с базой данных*
- ./configuration - провайдер настроек
    - test_config.ini - конфигурация
- ./test_data - провайдер тестовых данных
    - test_data.py - тестовые данные

### Зависимости

- requirements.txt

### Опции pytest

- pytest.ini

### Полезные ссылки

- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генерация .gitignore](https://www.toptal.com/developers/gitignore)
