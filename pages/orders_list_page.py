from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):

    def get_order_number_from_list(self):
        self.wait_close_element(OrderListPageLocators.MODAL)
        return self.wait_and_find_element(OrderListPageLocators.ORDER_NUMBER_LIST).text

    def get_orders_count_all(self):
        self.wait_close_element(OrderListPageLocators.MODAL)
        return int(self.wait_and_find_element(OrderListPageLocators.ORDERS_COUNT_ALL).text)

    def click_a_constructor(self):
        self.wait_and_find_element(OrderListPageLocators.A_CONSTRUCTOR).click()

    def get_orders_count_today(self):
        self.wait_close_element(OrderListPageLocators.MODAL)
        return int(self.wait_and_find_element(OrderListPageLocators.ORDERS_COUNT_TODAY).text)

    def find_order_number_in_work(self, order_number):
        in_work_path = OrderListPageLocators.IN_WORK[1].format(order_number)
        locator = (OrderListPageLocators.IN_WORK[0], in_work_path)
        return int(self.wait_and_find_element(locator).text)
