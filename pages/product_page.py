from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_button.click()

    def get_basket_total(self):
        return self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text

    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

    def get_product_name_in_message(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE
        ).text

    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    def should_be_basket_total_message(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_TOTAL_MESSAGE
        ), "Basket total message is not present but should be"

    def should_be_correct_price_in_basket_total_message(self, product_price):
        basket_total = self.get_basket_total()
        assert product_price == basket_total, (
            f"Expected basket total '{product_price}', "
            f"but got '{basket_total}'"
        )

    def should_be_correct_product_name_in_success_message(
            self,
            product_name
    ):
        product_name_in_message = self.get_product_name_in_message()
        assert product_name == product_name_in_message, (
            f"Expected product name '{product_name}' in success message, "
            f"but got '{product_name_in_message}'"
        )

    def should_be_success_message(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is not present but should be"

    def should_disappear_success_message(self):
        assert self.wait_for_element_to_disappear(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message did not disappear but should have"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is present but should not be"
