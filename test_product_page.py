"""
Test module for the product page.

Covers the login and sign-up page access, basket flow, and UI messages.
"""

import time

import pytest

from configuration import Links
from pages.basket_page import BasketPage
from pages.login_and_sign_up_page import LoginAndSignUpPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.mark.login_and_sign_up
class TestLoginAndSignUpFromProductPage:
    """Tests for the login/sign-up page access from the product page."""

    def test_guest_should_see_login_and_sign_up_link_on_product_page(
            self,
            browser
    ):
        """
        Check that a guest can see the login and sign-up link.

        Steps:
        1. Open the product page.
        2. Check for the presence of the login and sign-up link.
        """
        product_page = ProductPage(browser, Links.PRODUCT_PAGE)
        product_page.open()

        product_page.should_be_login_and_sign_up_link()

    def test_guest_can_go_to_login_and_sign_up_page_from_product_page(
            self,
            browser
    ):
        """
        Check that a guest can navigate to the login and sign-up page.

        Steps:
        1. Open the product page.
        2. Go to the login and sign-up page.
        3. Check that the current page is the login and sign-up page.
        """
        product_page = ProductPage(browser, Links.PRODUCT_PAGE)
        product_page.open()

        product_page.go_to_login_and_sign_up_page()
        login_and_sign_up_page = LoginAndSignUpPage(
            browser,
            browser.current_url
        )

        login_and_sign_up_page.should_be_login_and_sign_up_page()


@pytest.mark.basket_guest
class TestGuestAddToBasketFromProductPage:
    """Tests for adding a product from the product page by a guest."""

    def test_guest_cant_see_product_added_message(self, browser):
        """
        Check that there is no 'Product added' message before adding.

        Steps:
        1. Open the product page.
        2. Check that there is no 'Product added' message.
        """
        product_page = ProductPage(browser, Links.PRODUCT_PAGE)
        product_page.open()

        product_page.should_not_be_product_added_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(
            self,
            browser
    ):
        """
        Check that a guest's basket is empty by default.

        Steps:
        1. Open the product page.
        2. Go to the basket page.
        3. Check that the basket contains no items.
        4. Check for the presence of the 'Empty basket' message.
        """
        product_page = ProductPage(browser, Links.PRODUCT_PAGE)
        product_page.open()

        product_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)

        basket_page.should_be_empty()
        basket_page.should_be_empty_basket_message()

    # Generate a list of promotional product links for parametrization.
    # Offer 7 is marked with xfail because it is expected to fail
    # due to a known bug.
    PROMO_LINKS = [
        pytest.param(
            f"{Links.PRODUCT_PAGE}?promo=offer{n}",
            marks=pytest.mark.xfail if n == 7 else ()
        ) for n in range(10)
    ]

    @pytest.mark.parametrize("link", PROMO_LINKS)
    def test_guest_can_add_product_to_basket(self, browser, link):
        """
        Verify a guest can add a product and the correct one is added.

        Steps:
        1. Open the product page.
        2. Get the product name on the product page.
        3. Get the product price on the product page.
        4. Add the product to the basket.
        5. Solve the quiz in the alert.
        6. Verify the 'Product added' message is present.
        7. Verify the basket total message is present.
        8. Verify the product name in the message matches added product.
        9. Verify the basket total matches the added product's price.
        """
        product_page = ProductPage(browser, link)
        product_page.open()

        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()

        product_page.add_product_to_basket()

        product_page.solve_quiz_alert()

        product_page.should_be_product_added_message()
        product_page.should_be_basket_total_message()
        product_page.should_be_correct_product_name_in_product_added_message(
            product_name
        )
        product_page.should_be_correct_price_in_basket_total_message(
            product_price
        )

    @pytest.mark.xfail
    def test_guest_cant_see_product_added_message_after_adding_it_to_basket(
            self,
            browser
    ):
        """
        Check that there is no 'Product added' message after adding.

        Expected to fail because this message should appear.

        Steps:
        1. Open the product page.
        2. Add the product to the basket.
        3. Check that there is no 'Product added' message.
        """
        product_page = ProductPage(browser, Links.PRODUCT_PAGE)
        product_page.open()

        product_page.add_product_to_basket()

        product_page.should_not_be_product_added_message()

    @pytest.mark.xfail
    def test_product_added_message_disappears_after_adding_product_to_basket(
            self,
            browser
    ):
        """
        Check that the 'Product added' message disappears after adding.

        Expected to fail because this message should not disappear.

        Steps:
        1. Open the product page.
        2. Add the product to the basket.
        3. Check that the 'Product added' message disappears.
        """
        product_page = ProductPage(browser, Links.PRODUCT_PAGE)
        product_page.open()

        product_page.add_product_to_basket()

        product_page.should_disappear_product_added_message()


@pytest.mark.basket_user
class TestUserAddToBasketFromProductPage:
    """Tests for adding a product from its page for registered users."""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        Sign up a new user before each test in this class.

        Steps:
        1. Open the main page.
        2. Go to the login and sign-up page.
        3. Generate an email and a password using the current time.
        4. Perform the sign-up.
        5. Check that the user is authorized (the user icon is visible).
        """
        main_page = MainPage(browser, Links.MAIN_PAGE)
        main_page.open()

        main_page.go_to_login_and_sign_up_page()
        login_and_sign_up_page = LoginAndSignUpPage(
            browser,
            browser.current_url
        )

        timestamp = str(time.time())
        email = timestamp + "@fakemail.org"
        password = timestamp + "xyz"

        login_and_sign_up_page.sign_up_new_user(email, password)

        login_and_sign_up_page.should_be_authorized_user()

    def test_user_cant_see_product_added_message(self, browser):
        """
        Check that there is no 'Product added' message before adding.

        Steps:
        1. Open the product page.
        2. Check that there is no 'Product added' message.
        """
        product_page = ProductPage(browser, Links.PRODUCT_PAGE)
        product_page.open()

        product_page.should_not_be_product_added_message()

    def test_user_can_add_product_to_basket(self, browser):
        """
        Verify a user can add a product and the correct one is added.

        Steps:
        1. Open the product page.
        2. Get the product name on the product page.
        3. Get the product price on the product page.
        4. Add the product to the basket.
        5. Verify the 'Product added' message is present.
        6. Verify the basket total message is present.
        7. Verify the product name in the message matches added product.
        8. Verify the basket total matches the added product's price.
        """
        product_page = ProductPage(browser, Links.PRODUCT_PAGE)
        product_page.open()

        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()

        product_page.add_product_to_basket()

        product_page.should_be_product_added_message()
        product_page.should_be_basket_total_message()
        product_page.should_be_correct_product_name_in_product_added_message(
            product_name
        )
        product_page.should_be_correct_price_in_basket_total_message(
            product_price
        )
