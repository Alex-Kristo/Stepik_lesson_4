import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
import time


class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        page = LoginPage(driver, LoginPageLocators.LOGIN_LINK)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_user_can_add_product_to_cart(self, driver, link):
        page = ProductPage(driver, link)
        page.open()
        page.should_be_add_to_card_btn()
        add_to_cart_btn = page.driver.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_to_cart_btn.click()
        page.solve_quiz_and_get_code()
        assert page.find_product_name(*ProductPageLocators.PRODUCT_NAME_IN_CART) == \
            page.find_product_name(*ProductPageLocators.PRODUCT_NAME), "Product name does not match"
        assert page.find_product_price(*ProductPageLocators.PRODUCT_PRICE_IN_CART) == \
            page.find_product_price(*ProductPageLocators.PRODUCT_PRICE), "Product price does not match"

    def test_user_cant_see_success_message(self, driver):
        page = ProductPage(driver, ProductPageLocators.PRODUCT_LINK)
        page.open()
        page.is_not_element_present(*ProductPageLocators.ADD_TO_CART_ACCESS)


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_add_product_to_cart(driver, link):
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_card_btn()
    add_to_cart_btn = page.driver.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
    add_to_cart_btn.click()
    page.solve_quiz_and_get_code()
    page.product_name_in_cart()
    page.product_price_in_cart()


def test_guest_cant_see_success_message(driver):
    page = ProductPage(driver, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.is_not_element_present(*ProductPageLocators.ADD_TO_CART_ACCESS)


def test_guest_should_see_login_link_on_product_page(driver):
    page = ProductPage(driver, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(driver):
    page = ProductPage(driver, ProductPageLocators.PRODUCT_LINK)
    base_page_cart = page.go_to_cart()
    page_cart = CartPage(base_page_cart.driver, base_page_cart.url)
    page_cart.should_be_empty_cart()
