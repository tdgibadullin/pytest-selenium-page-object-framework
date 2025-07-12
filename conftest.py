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

    # Configure Chrome options to set the language.
    options = Options()
    options.add_experimental_option(
        'prefs',
        {'intl.accept_languages': user_language}
    )

    # Initialize the Chrome WebDriver with the specified options.
    browser = webdriver.Chrome(options=options)

    # Yield the browser instance to the test method.
    yield browser

    # Teardown: quit the browser after the test has finished.
    browser.quit()
