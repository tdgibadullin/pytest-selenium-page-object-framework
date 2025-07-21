"""
Sets up the pytest testing environment.

Defines the browser setup and the CLI option for the browser's locale.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    Add the custom --language command-line option to pytest.

    This enables running tests with a localized browser interface.
    """
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose browser language (e.g., en, es, fr, ru)."
    )


@pytest.fixture(scope="function")
def browser(request):
    """
    Launch and tear down a Chrome browser instance per test.

    Supports the --language CLI option to set the browser's locale.
    """
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs',
        {'intl.accept_languages': user_language}
    )

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()
