"""
Defines BasePage: a reusable base class for the page objects.

Encapsulates common actions and checks shared across the pages.
Covers navigation, element presence checks, and alert handling.
"""

import math

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators

# Default explicit wait timeout (in seconds).
DEFAULT_TIMEOUT = 5


class BasePage:
    """The base class for the page objects."""

    def __init__(self, browser, url):
        """Initialize the page object."""
        self.browser = browser
        self.url = url

    def open(self):
        """Open the page using the stored URL."""
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=DEFAULT_TIMEOUT):
        """Return True if the element appears within the timeout."""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=DEFAULT_TIMEOUT):
        """Return True if the element does not appear within timeout."""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=DEFAULT_TIMEOUT):
        """Return True if the element disappears within the timeout."""
        try:
            WebDriverWait(
                self.browser, timeout, 1, (TimeoutException,)
            ).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_login_and_sign_up_link(self):
        """Assert the presence of the login and sign-up link."""
        assert self.is_element_present(
            *BasePageLocators.LOGIN_AND_SIGN_UP_LINK
        ), "Login and sign-up link is not present but should be"

    def go_to_login_and_sign_up_page(self, timeout=DEFAULT_TIMEOUT):
        """Navigate to the login and sign-up page."""
        login_and_sign_up_link = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(BasePageLocators.LOGIN_AND_SIGN_UP_LINK)
        )
        login_and_sign_up_link.click()

    def should_be_authorized_user(self, timeout=DEFAULT_TIMEOUT):
        """Assert the user is authorized (the user icon is visible)."""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(BasePageLocators.USER_ICON)
            )
        except TimeoutException:
            assert False, (
                "User icon is not present, indicating unauthorized user"
            )

    def go_to_basket(self, timeout=DEFAULT_TIMEOUT):
        """Navigate to the basket page."""
        basket_button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(BasePageLocators.BASKET_BUTTON)
        )
        basket_button.click()

    def solve_quiz_alert(self, timeout=DEFAULT_TIMEOUT):
        """
        Solve the quiz presented in a JavaScript alert.

        Used on product pages with promo offers requiring a math answer.
        """
        alert = WebDriverWait(self.browser, timeout).until(
            EC.alert_is_present()
        )

        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))

        alert.send_keys(answer)
        alert.accept()
