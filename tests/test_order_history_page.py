import allure

from locators.order_history_page_locators import OrderHistoryPageLocators


class TestOrderHistoryPage:

    @allure.title('Проверка отображения модального окна с деталями заказа')
    def test_open_modal_order(self, login_and_create_order, order_history_page, main_page, profile_page):
        main_page.close_order_modal()
        main_page.click_button_account()
        main_page.wait_modal_close()
        profile_page.click_a_order_history()
        profile_page.wait_modal_close()
        order_history_page.open_order_details()
        order_history_page.wait_modal_close()
        assert order_history_page.wait_and_find_element(
            OrderHistoryPageLocators.MODAL_ORDER_DETAILS).text == "Выполнен"
