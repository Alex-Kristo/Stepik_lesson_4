from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    ADD_TO_CARD_BTN = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.XPATH, '//*[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@class="col-sm-6 product_main"]/p')
    PRODUCT_NAME_IN_CART = (By.XPATH, '(//*[@class ="alertinner "]/strong)[1]')
    PRODUCT_PRICE_IN_CART = (By.XPATH, '(//*[@class ="alertinner "]/p/strong)[1]')
