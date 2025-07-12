# Web Store Test Automation Framework (pytest & Selenium WebDriver)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![pytest](https://img.shields.io/badge/pytest-grey?logo=pytest)
![Selenium WebDriver](https://img.shields.io/badge/Selenium%20WebDriver-gray?logo=selenium&logoColor=43B02A)

[English Language](#english) | [Русский язык](#russian)

---
<a id="english"></a>
## Description

This project is a test automation framework for a demo web store, built using **pytest** and **Selenium WebDriver**. Initially developed as part of a test automation course, it has been significantly extended and refined beyond the course requirements to showcase advanced automation practices.

The framework's architecture is based on the **Page Object Model** pattern, which ensures modularity, readability, and ease of maintenance.

The tests cover various user scenarios for both guests and registered users.

The tests encompass:
- the visibility of the login and sign-up page link;
- navigation to the login and sign-up page; 
- adding a product to the basket; 
- success messages and basket content; 
- the behavior of an empty basket.

### Key Features

- **Test implementation based on Page Object Model:**
  - all web page–specific actions are encapsulated in Page Object classes, **separating test logic from UI interaction code**; 
  - tests focus on **high-level steps**, while checks are performed within Page Object methods, making the tests easy to read; 
  - all locators are defined in a separate `locators.py` module.
- **Centralized configuration:** all framework URLs are stored in a single `configuration.py` module.
- **Flexible browser configuration:** the `conftest.py` module includes a `browser` fixture that supports running tests in **different interface languages** via the `--language` command-line option.
- **Test data generation:** the `setup` fixture dynamically registers a new user before each test in the corresponding class, ensuring **test independence**.
- **Reliable waits:** the project uses **explicit waits** (`WebDriverWait`) to handle dynamic content loading and avoid flaky tests.
- **pytest integration:** the framework leverages powerful pytest features such as **parameterization**, **markers**, and **expected failures** (`xfail`).
- **Coverage of scenarios:** the project includes both **positive** and **negative** test cases for thorough functionality testing.
- **Comprehensive documentation:** all modules, functions, classes, and methods include **informative docstrings** and, where necessary, comments.
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

Using a virtual environment is recommended.

```bash
# Create and activate a virtual environment.
python -m venv venv
source venv/bin/activate  # For Windows (CMD): venv\Scripts\activate

# Install required packages.
pip install -r requirements.txt
```

*Note: Selenium WebDriver 4+ automatically handles the download and management of browser drivers (e.g., ChromeDriver) via its built-in Selenium Manager, so no manual driver setup is required in most cases.*

### 3. Run the tests

To run all tests, execute the following command in your terminal:

```bash
pytest
```

To run tests in a specific language (e.g., French), execute:

```bash
pytest --language=fr
```

To run only tests marked with a specific marker (e.g., `basket_user`), execute:

```bash
pytest -m basket_user
```

### Troubleshooting: Manual ChromeDriver Setup (if needed)

In most cases, Selenium WebDriver 4+ automatically downloads the required version of ChromeDriver.

However, if you encounter issues or are using an older version of Selenium WebDriver, manual installation of the driver may be required:
- Check your Google Chrome version (Three dots menu → Help → About Google Chrome).
- Download the corresponding version of ChromeDriver from the [official website](https://googlechromelabs.github.io/chrome-for-testing/).
- Unzip the archive and place the driver executable in a directory in your `PATH` (e.g., `/usr/local/bin` on Linux/macOS, or a folder in `PATH` on Windows).
- Make sure the correct version is installed by executing the following command in your terminal:
```bash
chromedriver --version
```

---

## License

This project is based on the materials from the course ["Test Automation with Selenium and Python"](https://stepik.org/course/575) (authors — Aleksey Pogibelev, Yulia Lyakh, and the Stepik Team), which is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The present project is distributed under the compatible [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) with proper attribution. The full text of the license is available in the `LICENSE` file in the project's root directory.

This project contains the original work of its author, as well as adapted and some unchanged materials from the aforementioned course.

---

## Author

© 2025 [Timur Gibadullin](https://github.com/tdgibadullin) ([tdgibadullin@gmail.com](mailto:tdgibadullin@gmail.com))

---
<a id="russian"></a>
## Описание

Этот проект представляет собой фреймворк для автоматизации тестирования демонстрационного интернет-магазина, созданный с использованием **pytest** и **Selenium WebDriver**. Первоначально проект был разработан в рамках курса по автоматизации тестирования, но впоследствии был значительно расширен и усовершенствован сверх требований курса, чтобы продемонстрировать продвинутые практики автоматизации.

Архитектура фреймворка основана на паттерне **Page Object Model**, что обеспечивает его модульность, читаемость и простоту в поддержке.

Тесты охватывают различные пользовательские сценарии как для гостей, так и для зарегистрированных пользователей.

Предусмотрены проверки в том числе:
- видимости ссылки на страницу логина и регистрации;
- переходов на страницу логина и регистрации;
- добавления товара в корзину;
- сообщений об успешном добавлении и содержимом корзины;
- поведения пустой корзины.

### Ключевые особенности

- **Реализация тестов по паттерну Page Object Model**:
  - все действия, специфичные для веб-страниц, инкапсулированы в Page Object-классах, что **отделяет логику тестов от кода взаимодействия с UI**;
  - тесты фокусируются на **высокоуровневых шагах**, а проверки выполняются внутри методов Page Object, что делает тесты легко читаемыми;
  - все локаторы вынесены в отдельный модуль `locators.py`.
- **Централизованная конфигурация:** URL фреймворка содержатся в едином модуле `configuration.py`.
- **Гибкая настройка браузера:** модуль `conftest.py` включает фикстуру `browser`, которая поддерживает запуск тестов с **разными языками интерфейса** через параметр командной строки `--language`.
- **Генерация тестовых данных:** фикстура `setup` динамически регистрирует нового пользователя перед каждым тестом в соответствующем классе, обеспечивая **независимость тестов**.
- **Надёжные ожидания:** фреймворк использует **явные ожидания** (`WebDriverWait`) для обработки динамической загрузки страниц и предотвращения нестабильных ("flaky") тестов.
- **Интеграция с pytest:** применяются мощные возможности pytest, такие как **параметризация**, **маркеры** и **ожидаемые падения** (`xfail`).
- **Покрытие сценариев:** включены как **позитивные**, так и **негативные** тест-кейсы для всесторонней проверки функциональности.
- **Качественная документация:** все модули, функции, классы и методы содержат **информативные англоязычные докстринги**, а также, при необходимости, комментарии.
- **Чистая структура фреймворка:** хорошо организованный репозиторий с понятной навигацией.

---

## Структура фреймворка

```text
pytest-selenium-page-object-framework/
├── .gitignore                    # Файлы и папки, игнорируемые Git
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

Рекомендуется использовать виртуальное окружение.

```bash
# Создание и активация виртуального окружения.
python -m venv venv
source venv/bin/activate  # Для Windows (CMD): venv\Scripts\activate

# Установка необходимых пакетов.
pip install -r requirements.txt
```

*Примечание: Selenium WebDriver 4+ автоматически управляет загрузкой и использованием драйверов браузеров (например, ChromeDriver) с помощью встроенного Selenium Manager, поэтому ручная установка драйвера в большинстве случаев не требуется.*

### 3. Запуск тестов

Чтобы запустить все тесты, выполните в терминале следующую команду:

```bash
pytest
```

Чтобы запустить тесты с определённым языком интерфейса (например, французским), выполните:

```bash
pytest --language=fr
```

Чтобы запустить только тесты с определённым маркером (например, `basket_user`), выполните:

```bash
pytest -m basket_user
```

### Устранение неполадок: ручная установка ChromeDriver (при необходимости)

В большинстве случаев Selenium WebDriver 4+ автоматически загружает нужную версию ChromeDriver.

Если вы столкнулись с проблемами или используете более старую версию Selenium WebDriver, может потребоваться ручная установка драйвера:
- Узнайте вашу версию Google Chrome (Настройка и управление Google Chrome (иконка с тремя точками) → Справка → О браузере Google Chrome).
- Скачайте соответствующую версию ChromeDriver с [официального сайта](https://googlechromelabs.github.io/chrome-for-testing/).
- Распакуйте архив и поместите исполняемый файл драйвера в директорию, доступную из `PATH` (например, `/usr/local/bin` на Linux/macOS, или в папку, добавленную в `PATH`, на Windows).
- Убедитесь, что нужная версия ChromeDriver установлена, выполнив следующую команду в терминале:
```bash
chromedriver --version
```

---

## Лицензия

Данный проект разработан на основе материалов курса ["Автоматизация тестирования с помощью Selenium и Python"](https://stepik.org/course/575) (авторы — Алексей Погибелев, Юлия Лях и команда Stepik), распространяющегося по лицензии [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Настоящий проект распространяется по совместимой лицензии [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) с надлежащим указанием авторства. Полный текст лицензии доступен в файле `LICENSE` в корневом каталоге проекта.

Данный проект содержит оригинальные наработки его автора, а также переработанные и отдельные неизменённые материалы указанного курса.

---

## Автор

© 2025 [Тимур Гибадуллин](https://github.com/tdgibadullin) ([tdgibadullin@gmail.com](mailto:tdgibadullin@gmail.com))
