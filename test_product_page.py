import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_test_guest_can_add_product_to_cart(driver, link):
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_card_btn()
    btn = page.driver.find_element(*ProductPageLocators.ADD_TO_CARD_BTN)
    btn.click()
    page.solve_quiz_and_get_code()
    assert page.find_product_name(*ProductPageLocators.PRODUCT_NAME_IN_CART) == \
        page.find_product_name(*ProductPageLocators.PRODUCT_NAME), "Product name does not match"
    assert page.find_product_price(*ProductPageLocators.PRODUCT_PRICE_IN_CART) == \
        page.find_product_price(*ProductPageLocators.PRODUCT_PRICE), "Product price does not match"
