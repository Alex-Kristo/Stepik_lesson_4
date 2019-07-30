from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BTN = (By.XPATH, "//span/a")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com"


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.XPATH, '//*[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@class="col-sm-6 product_main"]/p')
    PRODUCT_NAME_IN_CART = (By.XPATH, '(//*[@class ="alertinner "]/strong)[1]')
    PRODUCT_PRICE_IN_CART = (By.XPATH, '(//*[@class ="alertinner "]/p/strong)[1]')
    ADD_TO_CART_ACCESS = (By.XPATH, '(//*[@class ="alertinner "])[1]')


class CartPageLocators(object):
    PRODUCTS_IN_CART = (By.CSS_SELECTOR, '.col-sm-6.h3')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    CART_LINK = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
