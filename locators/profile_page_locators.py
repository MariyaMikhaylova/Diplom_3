from selenium.webdriver.common.by import By


class ProfilePageLocators:

    A_HISTORY = (By.XPATH, './/a[@href = "/account/order-history"]')  # гиперссылка истории заказов
    BUTTON_EXIT = (By.XPATH, '//button[text() = "Выход"]')  # кнопка выхода из аккаунта
    A_PROFILE = (By.XPATH, './/a[@href = "/account/profile"]')  # гиперссылка «Профиль»
