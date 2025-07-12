"""
Defines BasketPage: the page object class for the basket page.

Includes assertions for verifying the basket's empty state.
"""

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """The page object class for the basket page."""

    def should_be_empty(self):
        """Assert that the basket contains no products."""
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Basket is not empty but should be"

    def should_be_empty_basket_message(self):
        """Assert the presence of the 'Empty basket' message."""
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ), "'Empty basket' message is not present but should be"
