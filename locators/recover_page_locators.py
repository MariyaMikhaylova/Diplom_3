from selenium.webdriver.common.by import By


class RecoverPageLocators:

    EMAIL = (By.XPATH, '//input[@name="name"]')  # поле ввода email
    BUTTON_RECOVER = (By.XPATH, '//button[text() = "Восстановить"]')  # кнопка Восстановить
