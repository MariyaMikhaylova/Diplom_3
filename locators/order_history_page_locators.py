from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    ORDER = (By.XPATH, '//*[@class="OrderHistory_orderHistory__qy1VB"]//a')  # карточка заказа
    ORDER_NUMBER = (By.XPATH, '//*[@class="OrderHistory_orderHistory__qy1VB"]//a/div/child::p')  # номер заказа
    MODAL_ORDER_DETAILS = (By.XPATH, '//*[@class="Modal_modal__container__Wo2l_"]//p[text() = "Выполнен"]')  # Модальное окно деталей заказа
    MODAL = (By.XPATH, '//div[contains(@class, "Modal_modal_overlay__x2ZCr")]/parent::div')  # Модальное окно
    A_ORDERS_LIST = (By.XPATH, './/a[@href = "/feed"]')  # гиперссылка Лента заказов
