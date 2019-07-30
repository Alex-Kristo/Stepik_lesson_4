from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_card_btn(self):
        self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN)
        assert True

    def find_product_name(self, how, what):
        self.is_element_present(how, what)
        assert True
        product_name = self.driver.find_element(how, what)
        return product_name.text

    def find_product_price(self, how, what):
        self.is_element_present(how, what)
        assert True
        product_price = self.driver.find_element(how, what)
        return product_price.text

    def product_name_in_cart(self):
        assert self.find_product_name(*ProductPageLocators.PRODUCT_NAME_IN_CART) == \
            self.find_product_name(*ProductPageLocators.PRODUCT_NAME), "Product name does not match"

    def product_price_in_cart(self):
        assert self.find_product_price(*ProductPageLocators.PRODUCT_PRICE_IN_CART) == \
            self.find_product_price(*ProductPageLocators.PRODUCT_PRICE), "Product price does not match"
