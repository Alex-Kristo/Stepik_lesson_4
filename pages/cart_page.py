from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCTS_IN_CART), "Your basket is not empty"
        empty_cart_message = self.driver.find_element(*CartPageLocators.EMPTY_CART_MESSAGE)
        self.substring_in(empty_cart_message.text, "Your basket is empty")
