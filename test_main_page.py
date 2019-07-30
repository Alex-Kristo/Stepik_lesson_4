import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
from .pages.cart_page import CartPage


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver, MainPageLocators.MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, driver):
        page = MainPage(driver, MainPageLocators.MAIN_PAGE_LINK)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(driver):
    page = MainPage(driver, MainPageLocators.MAIN_PAGE_LINK)
    base_page_cart = page.go_to_cart()
    page_cart = CartPage(base_page_cart.driver, base_page_cart.url)
    page_cart.should_be_empty_cart()
