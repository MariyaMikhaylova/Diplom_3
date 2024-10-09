from selenium.webdriver.common.by import By


class OrderListPageLocators:

    ORDER_NUMBER_LIST = (By.XPATH, '//*[@class = "OrderFeed_list__OLh59"]//p')  # номер заказа в карточке заказа
    ORDERS_COUNT_ALL = (By.XPATH, '//p[text() = "Выполнено за все время:"]/following-sibling::p')  # счетчик заказов за все время
    ORDERS_COUNT_TODAY = (By.XPATH, '//p[text() = "Выполнено за сегодня:"]/following-sibling::p')  # счетчик заказов за сегодня
    MODAL = (By.XPATH, '//div[contains(@class, "Modal_modal_overlay__x2ZCr")]/parent::div')  # Модальное окно
    A_CONSTRUCTOR = (By.XPATH, './/p[text() = "Конструктор"]/parent::a')  # гиперссылка Конструктор
    IN_WORK = (By.XPATH, '//*[@class = "OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]//li[contains(.,"{}")]')  # номер заказа в работе
