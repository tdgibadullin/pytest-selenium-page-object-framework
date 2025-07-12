"""
Contains ProductPage: the page object class for the product page.

Includes methods for product interaction and basket message validation.
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage, DEFAULT_TIMEOUT
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """The page object class for the product page."""

    def get_product_name(self, timeout=DEFAULT_TIMEOUT):
        """Return the product name from the product page."""
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(ProductPageLocators.PRODUCT_NAME)
        ).text

    def get_product_price(self, timeout=DEFAULT_TIMEOUT):
        """Return the product price from the product page."""
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(ProductPageLocators.PRODUCT_PRICE)
        ).text

    def get_product_name_in_message(self, timeout=DEFAULT_TIMEOUT):
        """Return the product name from the 'Product added' message."""
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(
                ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        ).text

    def get_basket_total(self, timeout=DEFAULT_TIMEOUT):
        """Return the basket total from the basket total message."""
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(ProductPageLocators.BASKET_TOTAL)
        ).text

    def add_product_to_basket(self, timeout=DEFAULT_TIMEOUT):
        """Add the product to the basket."""
        add_button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(
                ProductPageLocators.ADD_TO_BASKET_BUTTON
            )
        )
        add_button.click()

    def should_be_product_added_message(self):
        """Assert the presence of the 'Product added' message."""
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_ADDED_MESSAGE
        ), "'Product added' message is not present but should be"

    def should_not_be_product_added_message(self):
        """Assert the absence of the 'Product added' message."""
        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_ADDED_MESSAGE
        ), "'Product added' message is present but should not be"

    def should_disappear_product_added_message(self):
        """Assert that the 'Product added' message disappears."""
        assert self.is_disappeared(
            *ProductPageLocators.PRODUCT_ADDED_MESSAGE
        ), "'Product added' message did not disappear but should have"

    def should_be_basket_total_message(self):
        """Assert the presence of the basket total message."""
        assert self.is_element_present(
            *ProductPageLocators.BASKET_TOTAL_MESSAGE
        ), "Basket total message is not present but should be"

    def should_be_correct_product_name_in_product_added_message(
            self,
            product_name
    ):
        """Assert the product name in message matches added product."""
        product_name_in_message = self.get_product_name_in_message()
        assert product_name == product_name_in_message, (
            f"Expected product name '{product_name}' in 'Product added' "
            f"message, but got '{product_name_in_message}'"
        )

    def should_be_correct_price_in_basket_total_message(self, product_price):
        """Assert the basket total matches the added product's price."""
        basket_total = self.get_basket_total()
        assert product_price == basket_total, (
            f"Expected basket total '{product_price}', "
            f"but got '{basket_total}'"
        )
