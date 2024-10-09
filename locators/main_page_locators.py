from selenium.webdriver.common.by import By


class MainPageLocators:

    TITLE = (By.XPATH, './/h1[text() = "Соберите бургер"]')  # заголовок "Соберите бургер"
    BUTTON_ACCOUNT = (By.XPATH, './/a[@href = "/account"]')  # кнопка входа в личный кабинет
    MODAL = (By.XPATH, '//div[contains(@class, "Modal_modal_overlay__x2ZCr")]/parent::div')  # Модальное окно
    A_ORDERS_LIST = (By.XPATH, './/a[@href = "/feed"]')  # гиперссылка Лента заказов
    BURGER_CONSTRUCTOR = (By.XPATH, './/ul[@class = "BurgerConstructor_basket__list__l9dp_"]')  # Конструктор бургера
    MODAL_INGREDIENT_TITLE = (By.XPATH, './/*[text() = "Детали ингредиента"]')  # Заголовок модального окна Детали ингредиента
    MODAL_INGREDIENT_CLOSE = (By.XPATH, '//div[contains(@class, "Modal_modal__container__Wo2l_")]/child::button')  # Закрытие модального окна Детали ингредиента
    COUNTER_CRATER_BUN = (By.XPATH, './/a[@href = "/ingredient/61c0c5a71d1f82001bdaaa6c"]//child::p[text() = "2"]')  # Каунтер Краторная булка N-200i
    BUTTON_CREATE_ORDER = (By.XPATH, './/button[text() = "Оформить заказ"]')  # Кнопка Оформить заказ
    TEXT_IDENTITY_ORDER = (By.XPATH, './/*[text() = "идентификатор заказа"]')  # Надпись идентификатор заказа
    ORDER_NUMBER = (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//h2')  # номер заказа
    CLOSE_ORDER_BUTTON = (By.XPATH, '//button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')  # закрытие модального окна заказа
    CRATER_BUN = (By.XPATH, './/a[@href = "/ingredient/61c0c5a71d1f82001bdaaa6c"]')  # Краторная булка N-200i
    SPACE_SAUSE = (By.XPATH, './/a[@href = "/ingredient/61c0c5a71d1f82001bdaaa73"]')  # Соус фирменный Space Sauce
    FILE_LUM_T = (By.XPATH, './/a[@href = "/ingredient/61c0c5a71d1f82001bdaaa6e"]')  # Филе Люминесцентного тетраодонтимформа
    FALL_TREE = (By.XPATH, './/a[@href = "/ingredient/61c0c5a71d1f82001bdaaa77"]')  # Плоды Фалленианского дерева
    ORDER_MODAL = (By.XPATH, '//div[@class="Modal_modal__container__Wo2l_"]')  # Модальное окно заказа
