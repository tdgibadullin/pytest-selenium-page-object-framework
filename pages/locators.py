from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class MainPageLocators:
    pass

class ProductPageLocators:
    # Кнопка добавления в корзину
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # Основная информация о товаре
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    # Сообщения после добавления в корзину
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info")
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1) .alertinner"
    )

    # Текст в сообщениях после добавления в корзину
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")
    PRODUCT_NAME_IN_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success:nth-of-type(1) strong"
    )
