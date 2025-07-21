# Web Store End-to-End Test Automation Framework (pytest & Selenium WebDriver)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![pytest](https://img.shields.io/badge/pytest-grey?logo=pytest)
![Selenium WebDriver](https://img.shields.io/badge/Selenium%20WebDriver-gray?logo=selenium&logoColor=43B02A)

[English language](#english) | [Русский язык](#russian)

---
<a id="english"></a>
## Description

This project is an end-to-end test automation framework for a demo web store, built using **pytest** and **Selenium WebDriver**.

Initially developed as part of completing a test automation course, it has been significantly extended and refined beyond the course requirements to showcase advanced automation practices.

The framework's architecture is based on the **Page Object Model** pattern, which ensures modularity, readability, and ease of maintenance.

The tests cover various scenarios for both guests and registered users. The checks include:
- visibility of the login and sign-up page link;
- navigation to the login and sign-up page; 
- adding a product to the basket; 
- success messages and basket content; 
- behavior of an empty basket.

### Key Features

- **Test implementation based on Page Object Model:**
  - all the web page–specific actions are encapsulated in the Page Object classes, **separating test logic from UI interaction code**; 
  - the tests focus on **high-level steps**, while the lower-level checks are performed within the Page Object methods, making the tests easy to read; 
  - all the locators are defined in a separate `locators.py` module.
- **Centralized configuration:** all the framework URLs are stored in a single `configuration.py` module.
- **Flexible browser configuration:** the `conftest.py` module includes a `browser` fixture that supports running tests in **different interface languages** via the `--language` command-line option.
- **Test data generation:** the `setup` fixture dynamically registers a new user before each test in the corresponding class, ensuring **test independence**.
- **Reliable waits:** the project uses **explicit waits** (`WebDriverWait`) to handle dynamic content loading and avoid flaky tests.
- **Advanced pytest integration:** the framework leverages powerful pytest features such as **parameterization**, **expected failures** (`xfail`), and **custom markers**.
- **Coverage of scenarios:** the project includes both **positive** and **negative** test cases for a thorough functionality testing.
- **Comprehensive documentation:** all the modules, functions, classes, and methods include **informative docstrings** and, where necessary, comments.
- **Clean framework structure:** a well-organized repository with intuitive navigation.

---

## Framework Structure

```text
pytest-selenium-page-object-framework/
├── .gitignore                    # Files and directories ignored by Git
├── __init__.py                   # Marks the directory as a Python package
├── configuration.py              # All the framework URLs
├── conftest.py                   # pytest fixtures and hooks (browser setup)
├── LICENSE                       # License under which the framework is distributed
├── pytest.ini                    # pytest configuration (custom markers)
├── README.md                     # Framework description and usage instructions
├── requirements.txt              # Framework dependencies
├── test_main_page.py             # Tests for the web store’s main page
├── test_product_page.py          # Tests for the product page
└── pages/                        # Package with the Page Object classes and locators
    ├── __init__.py               # Marks the directory as a Python package
    ├── base_page.py              # BasePage class with shared methods
    ├── basket_page.py            # Page Object class for the basket page
    ├── locators.py               # All the page locators
    ├── login_and_sign_up_page.py # Page Object class for the login and sign-up page
    ├── main_page.py              # Page Object class for the web store's main page
    └── product_page.py           # Page Object class for the product page
```

---

## Tech Stack

- **Language:** Python 3.13
- **Test runner:** pytest
- **Browser automation:** Selenium WebDriver
- **Target browser:** Google Chrome + ChromeDriver

---

## Installation and Usage

*This test automation framework requires Google Chrome to be installed on your system.*

### 1. Clone the repository

```bash
git clone https://github.com/tdgibadullin/pytest-selenium-page-object-framework.git
cd pytest-selenium-page-object-framework
```

### 2. Install dependencies

Create a virtual environment:

```bash 
python -m venv venv # If the "python" command is not found, try "python3"
```

Activate the virtual environment:

```bash 
# For macOS/Linux
source venv/bin/activate

# For Windows (CMD)
venv\Scripts\activate.bat

# For Windows (PowerShell)
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the tests

To run all tests:

```bash
pytest
```

To run tests in a specific language (e.g., French):

```bash
pytest --language=fr
```

To run only tests marked with a specific marker (e.g., `basket_user`):

```bash
pytest -m basket_user
```

### Troubleshooting: Manual ChromeDriver Installation (If Needed)

In most cases, Selenium WebDriver 4+ automatically downloads the appropriate version of ChromeDriver.

If you encounter issues or are using an older version of Selenium WebDriver, manual installation of the driver may be required:
- Check your Google Chrome version (Three-dot menu → Help → About Google Chrome).
- Download the matching version of ChromeDriver from the [official website](https://googlechromelabs.github.io/chrome-for-testing/).
- Extract the archive and move the driver executable to a directory listed in the `PATH` environment variable.
- Verify that the correct version of ChromeDriver is installed:

```bash
chromedriver --version
```

---

## License

This project is based on the materials from the course ["Test Automation using Selenium and Python"](https://stepik.org/course/575) (authors — Aleksey Pogibelev, Yulia Lyakh, and the Stepik Team), which is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The present project is distributed under the compatible [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). The full text of the license is available in the `LICENSE` file in the project's root directory.

This project contains the original work of its author, as well as adapted and some unchanged materials from the aforementioned course.

---

## Author

© [Timur Gibadullin](https://github.com/tdgibadullin) ([tdgibadullin@gmail.com](mailto:tdgibadullin@gmail.com)), 2025

---
<a id="russian"></a>
## Описание

Этот проект представляет собой фреймворк для автоматизации end-to-end тестирования демонстрационного интернет-магазина, созданный с использованием **pytest** и **Selenium WebDriver**.

Первоначально проект был разработан в рамках прохождения курса по автоматизации тестирования, но впоследствии был значительно расширен и усовершенствован сверх требований курса, чтобы продемонстрировать продвинутые практики автоматизации.

Архитектура фреймворка основана на паттерне **Page Object Model**, что обеспечивает его модульность, читаемость и простоту в поддержке.

Тесты охватывают различные сценарии как для гостей, так и для зарегистрированных пользователей. Предусмотрены проверки в том числе:
- видимости ссылки на страницу логина и регистрации;
- переходов на страницу логина и регистрации;
- добавления товара в корзину;
- сообщений об успешном добавлении и содержимом корзины;
- поведения пустой корзины.

### Ключевые особенности

- **Реализация тестов по паттерну Page Object Model**:
  - все действия, специфичные для веб-страниц, инкапсулированы в Page Object-классах, что **отделяет логику тестов от кода взаимодействия с UI**;
  - тесты фокусируются на **высокоуровневых шагах**, а проверки более низкого уровня выполняются внутри методов Page Object, что делает тесты легко читаемыми;
  - все локаторы вынесены в отдельный модуль `locators.py`.
- **Централизованная конфигурация:** URL фреймворка содержатся в едином модуле `configuration.py`.
- **Гибкая настройка браузера:** модуль `conftest.py` включает фикстуру `browser`, которая поддерживает запуск тестов с **разными языками интерфейса** через параметр командной строки `--language`.
- **Генерация тестовых данных:** фикстура `setup` динамически регистрирует нового пользователя перед каждым тестом в соответствующем классе, обеспечивая **независимость тестов**.
- **Надёжные ожидания:** фреймворк использует **явные ожидания** (`WebDriverWait`) для обработки динамической загрузки страниц и предотвращения нестабильных ("flaky") тестов.
- **Расширенная интеграция с pytest:** применяются мощные возможности pytest, такие как **параметризация**, **ожидаемые падения** (`xfail`) и **пользовательские маркеры**.
- **Покрытие сценариев:** включены как **позитивные**, так и **негативные** тест-кейсы для всесторонней проверки функциональности.
- **Качественная документация:** все модули, функции, классы и методы содержат **информативные англоязычные докстринги**, а также, при необходимости, комментарии.
- **Чистая структура фреймворка:** хорошо организованный репозиторий с понятной навигацией.

---

## Структура фреймворка

```text
pytest-selenium-page-object-framework/
├── .gitignore                    # Файлы и директории, игнорируемые Git
├── __init__.py                   # Обозначает директорию как Python-пакет
├── configuration.py              # Все URL фреймворка
├── conftest.py                   # Фикстуры и хуки pytest (настройка браузера)
├── LICENSE                       # Лицензия, по которой распространяется фреймворк
├── pytest.ini                    # Конфигурация pytest (пользовательские маркеры)
├── README.md                     # Описание фреймворка и инструкции по запуску
├── requirements.txt              # Зависимости фреймворка
├── test_main_page.py             # Тесты для главной страницы магазина
├── test_product_page.py          # Тесты для страницы товара
└── pages/                        # Пакет с Page Object-классами и их локаторами
    ├── __init__.py               # Обозначает директорию как Python-пакет
    ├── base_page.py              # Базовый класс BasePage с общими методами
    ├── basket_page.py            # Page Object-класс для страницы корзины
    ├── locators.py               # Все локаторы страниц
    ├── login_and_sign_up_page.py # Page Object-класс для страницы логина и регистрации
    ├── main_page.py              # Page Object-класс для главной страницы магазина
    └── product_page.py           # Page Object-класс для страницы товара
```

---

## Стек технологий

- **Язык**: Python 3.13
- **Тестовый раннер**: pytest
- **Автоматизация браузера**: Selenium WebDriver
- **Целевой браузер**: Google Chrome + ChromeDriver

---

## Установка и запуск

*Для работы этого фреймворка требуется установленный Google Chrome.*

### 1. Клонирование репозитория

```bash
git clone https://github.com/tdgibadullin/pytest-selenium-page-object-framework.git
cd pytest-selenium-page-object-framework
```

### 2. Установка зависимостей

Создайте виртуальное окружение:

```bash 
python -m venv venv # Если команда "python" не найдена, попробуйте "python3"
```

Активируйте виртуальное окружение:

```bash 
# Для macOS/Linux
source venv/bin/activate

# Для Windows (CMD)
venv\Scripts\activate.bat

# Для Windows (PowerShell)
venv\Scripts\Activate.ps1
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

### 3. Запуск тестов

Запуск всех тестов:

```bash
pytest
```

Запуск тестов с определённым языком интерфейса (например, французским):

```bash
pytest --language=fr
```

Запуск тестов с определённым маркером (например, `basket_user`):

```bash
pytest -m basket_user
```

### Устранение неполадок: ручная установка ChromeDriver (при необходимости)

В большинстве случаев Selenium WebDriver 4+ автоматически загружает подходящую версию ChromeDriver.

Если вы столкнулись с проблемами или используете более старую версию Selenium WebDriver, может потребоваться ручная установка драйвера:
- Определите вашу версию Google Chrome (Настройка и управление Google Chrome (иконка с тремя точками) → Справка → О браузере Google Chrome).
- Скачайте соответствующую версию ChromeDriver с [официального сайта](https://googlechromelabs.github.io/chrome-for-testing/).
- Распакуйте архив и поместите исполняемый файл драйвера в директорию, указанную в переменной окружения `PATH`.
- Убедитесь, что нужная версия ChromeDriver установлена:

```bash
chromedriver --version
```

---

## Лицензия

Данный проект разработан на основе материалов курса ["Автоматизация тестирования с помощью Selenium и Python"](https://stepik.org/course/575) (авторы — Алексей Погибелев, Юлия Лях и команда Stepik), распространяющегося по лицензии [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Настоящий проект распространяется по совместимой лицензии [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). Полный текст лицензии доступен в файле `LICENSE` в корневом каталоге проекта.

Данный проект содержит оригинальные наработки его автора, а также переработанные и отдельные неизменённые материалы указанного курса.

---

## Автор

© [Тимур Гибадуллин](https://github.com/tdgibadullin) ([tdgibadullin@gmail.com](mailto:tdgibadullin@gmail.com)), 2025
