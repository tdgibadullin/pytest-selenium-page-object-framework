"""
Defines LoginAndSignUpPage: the page object class for login and sign-up.

Provides methods for the URL/form assertions and new user sign-up.
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage, DEFAULT_TIMEOUT
from .locators import LoginAndSignUpPageLocators


class LoginAndSignUpPage(BasePage):
    """The page object class for the login and sign-up page."""

    def should_be_login_and_sign_up_page(self):
        """Assert the current page is the login and sign-up page."""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_sign_up_form()

    def should_be_login_url(self):
        """Assert that the current URL contains 'login'."""
        assert "login" in self.browser.current_url, (
            "'login' substring is not present in current URL"
        )

    def should_be_login_form(self):
        """Assert the presence of the login form."""
        assert self.is_element_present(
            *LoginAndSignUpPageLocators.LOGIN_FORM
        ), "Login form is not present"

    def should_be_sign_up_form(self):
        """Assert the presence of the sign-up form."""
        assert self.is_element_present(
            *LoginAndSignUpPageLocators.SIGN_UP_FORM
        ), "Sign-up form is not present"

    def sign_up_new_user(self, email, password, timeout=DEFAULT_TIMEOUT):
        """
        Fill the sign-up form and submit it.

        Uses the email and password generated in the setup() fixture.
        """
        email_input = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(
                LoginAndSignUpPageLocators.EMAIL_INPUT
            )
        )
        email_input.send_keys(email)

        password_input_1 = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(
                LoginAndSignUpPageLocators.PASSWORD_INPUT_1
            )
        )
        password_input_1.send_keys(password)

        password_input_2 = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(
                LoginAndSignUpPageLocators.PASSWORD_INPUT_2
            )
        )
        password_input_2.send_keys(password)

        sign_up_button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(
                LoginAndSignUpPageLocators.SIGN_UP_BUTTON
            )
        )
        sign_up_button.click()
