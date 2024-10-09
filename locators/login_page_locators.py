from selenium.webdriver.common.by import By


class LoginPageLocators:

    RECOVER_PASSWORD = (By.XPATH, '//a[@href = "/forgot-password"]')  # гиперссылка Восстановить пароль
    EMAIL = (By.XPATH, './/label[text() = "Email"]/following-sibling::input')  # Почта
    PASSWORD = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input')  # Пароль
    BUTTON_ENTER = (By.XPATH, './/button[text() = "Войти"]')  # Кнопка "Войти"
    A_CONSTRUCTOR = (By.XPATH, './/p[text() = "Конструктор"]/parent::a')  # гиперссылка Конструктор
