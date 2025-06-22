import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com"
BASE_PRODUCT_LINK = ("http://selenium1py.pythonanywhere.com/catalogue/"
                     "coders-at-work_207/")
OTHER_PRODUCT_LINK = ("http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
                      "the-city-and-the-stars_95/")


@pytest.mark.need_review
@pytest.mark.parametrize(
    'link', [
        f"{BASE_PRODUCT_LINK}?promo=offer0",
        f"{BASE_PRODUCT_LINK}?promo=offer1",
        f"{BASE_PRODUCT_LINK}?promo=offer2",
        f"{BASE_PRODUCT_LINK}?promo=offer3",
        f"{BASE_PRODUCT_LINK}?promo=offer4",
        f"{BASE_PRODUCT_LINK}?promo=offer5",
        f"{BASE_PRODUCT_LINK}?promo=offer6",
        pytest.param(
            f"{BASE_PRODUCT_LINK}?promo=offer7",
            marks=pytest.mark.xfail
        ),
        f"{BASE_PRODUCT_LINK}?promo=offer8",
        f"{BASE_PRODUCT_LINK}?promo=offer9"
    ]
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_success_message()
    page.should_be_basket_total_message()
    page.should_be_correct_product_name_in_success_message(product_name)
    page.should_be_correct_price_in_basket_total_message(product_price)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    page = ProductPage(browser, BASE_PRODUCT_LINK)
    page.open()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, BASE_PRODUCT_LINK)
    page.open()

    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappears_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BASE_PRODUCT_LINK)
    page.open()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, OTHER_PRODUCT_LINK)
    page.open()

    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, OTHER_PRODUCT_LINK)
    page.open()

    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, BASE_PRODUCT_LINK)
    page.open()

    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_be_empty_basket_message()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()

        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        timestamp = str(time.time())
        email = timestamp + "@fakemail.org"
        password = timestamp + "xyz"

        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, BASE_PRODUCT_LINK)
        page.open()

        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, BASE_PRODUCT_LINK)
        page.open()

        product_name = page.get_product_name()
        product_price = page.get_product_price()

        page.add_product_to_basket()

        page.should_be_success_message()
        page.should_be_basket_total_message()
        page.should_be_correct_product_name_in_success_message(product_name)
        page.should_be_correct_price_in_basket_total_message(product_price)
