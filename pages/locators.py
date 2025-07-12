"""Centralized definition of locators used by the page objects."""

from selenium.webdriver.common.by import By


class BasePageLocators:
    """Locators that are used across multiple pages."""

    LOGIN_AND_SIGN_UP_LINK = (By.ID, "login_link")
    USER_ICON = (By.CLASS_NAME, "icon-user")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")


class MainPageLocators:
    """Locators for the main page."""
    # This class is empty as the main page uses only the base locators.

    pass


class LoginAndSignUpPageLocators:
    """Locators for the login and sign-up page."""

    LOGIN_FORM = (By.ID, "login_form")
    SIGN_UP_FORM = (By.ID, "register_form")

    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT_1 = (By.ID, "id_registration-password1")
    PASSWORD_INPUT_2 = (By.ID, "id_registration-password2")

    SIGN_UP_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    """Locators for the product page."""

    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    # Messages after adding a product to the basket.
    PRODUCT_ADDED_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1) .alertinner"
    )
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info")

    # Text within the messages after adding a product to the basket.
    PRODUCT_NAME_IN_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1) strong"
    )
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")


class BasketPageLocators:
    """Locators for the basket page."""

    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
