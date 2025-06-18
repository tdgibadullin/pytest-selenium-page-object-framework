from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    USER_ICON = (By.CLASS_NAME, "icon-user")

class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class LoginPageLocators:
    EMAIL_INPUT = (By.ID, "id_registration-email")
    LOGIN_FORM = (By.ID, "login_form")
    PASSWORD_INPUT_1 = (By.ID, "id_registration-password1")
    PASSWORD_INPUT_2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    REGISTER_FORM = (By.ID, "register_form")

class MainPageLocators:
    pass

class ProductPageLocators:
    # Кнопка добавления в корзину
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    # Основная информация о товаре
    PRODUCT_NAME = (By.TAG_NAME, "h1")
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
