from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    # Основная информация о товаре
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    # Кнопка добавления в корзину
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # Сообщения после добавления в корзину
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1) .alertinner"
    )
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info")

    # Текст в сообщениях после добавления в корзину
    PRODUCT_NAME_IN_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1) strong"
    )
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")
