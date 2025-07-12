"""
Test module for the web store's main page.

Covers access to the login and sign-up page and the guest basket state.
"""

import pytest

from configuration import Links
from pages.basket_page import BasketPage
from pages.login_and_sign_up_page import LoginAndSignUpPage
from pages.main_page import MainPage


@pytest.mark.login_and_sign_up
class TestLoginAndSignUpFromMainPage:
    """Tests for accessing the login/sign-up page from the main page."""

    def test_guest_should_see_login_and_sign_up_link_on_main_page(
            self,
            browser
    ):
        """
        Check that a guest can see the login and sign-up link.

        Steps:
        1. Open the main page.
        2. Check for the presence of the login and sign-up link.
        """
        main_page = MainPage(browser, Links.MAIN_PAGE)
        main_page.open()

        main_page.should_be_login_and_sign_up_link()

    def test_guest_can_go_to_login_and_sign_up_page_from_main_page(
            self,
            browser
    ):
        """
        Check that a guest can navigate to the login and sign-up page.

        Steps:
        1. Open the main page.
        2. Go to the login and sign-up page.
        3. Check that the current page is the login and sign-up page.
        """
        main_page = MainPage(browser, Links.MAIN_PAGE)
        main_page.open()

        main_page.go_to_login_and_sign_up_page()
        login_and_sign_up_page = LoginAndSignUpPage(
            browser,
            browser.current_url
        )

        login_and_sign_up_page.should_be_login_and_sign_up_page()


@pytest.mark.basket_guest
class TestGuestBasketFromMainPage:
    """Tests for the basket accessed by a guest from the main page."""

    def test_guest_cant_see_product_in_basket_opened_from_main_page(
            self,
            browser
    ):
        """
        Check that a guest's basket is empty by default.

        Steps:
        1. Open the main page.
        2. Go to the basket page.
        3. Check that the basket contains no items.
        4. Check for the presence of the 'Empty basket' message.
        """
        main_page = MainPage(browser, Links.MAIN_PAGE)
        main_page.open()

        main_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)

        basket_page.should_be_empty()
        basket_page.should_be_empty_basket_message()
