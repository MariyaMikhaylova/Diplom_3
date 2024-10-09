from selenium.webdriver.common.by import By


class ResetPasswordLocators:

    BUTTON_SAVE = (By.XPATH, '//button[text() = "Сохранить"]')  # кнопка Сохранить
    SWG_PASSWORD = (By.XPATH, '//*[@class = "input__icon input__icon-action"]/child::*')  # контейнер просмотра/скрытия пароля
    SHOW_PASSWORD = (By.XPATH, '//*[@class = "input pr-6 pl-6 input_type_text input_size_default input_status_active"]')  # отображение пароля
