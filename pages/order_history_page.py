from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):

    def open_order_details(self):
        self.wait_and_find_element(OrderHistoryPageLocators.ORDER).click()

    def get_order_number(self):
        return self.wait_and_find_element(OrderHistoryPageLocators.ORDER_NUMBER).text

    def click_a_order_list(self):
        self.wait_close_element(OrderHistoryPageLocators.MODAL)
        self.wait_and_find_element(OrderHistoryPageLocators.A_ORDERS_LIST).click()
