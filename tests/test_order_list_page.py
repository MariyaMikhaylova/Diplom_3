import allure


class TestOrderListPage:

    @allure.title('Проверка отображения заказа из истории заказов в листе заказов')
    def test_find_order_on_order_list_page(self,
                                           login_and_create_order,
                                           order_history_page,
                                           main_page,
                                           profile_page,
                                           orders_list_page):
        main_page.close_order_modal()
        main_page.click_button_account()
        main_page.wait_modal_close()
        profile_page.click_a_order_history()
        profile_page.wait_modal_close()
        order_number = order_history_page.get_order_number()
        order_history_page.click_a_order_list()
        order_number_from_list = orders_list_page.get_order_number_from_list()
        assert order_number == order_number_from_list

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_count_all(self, login, main_page, orders_list_page):
        main_page.click_a_order_list()
        count_before_order = orders_list_page.get_orders_count_all()
        orders_list_page.click_a_constructor()
        main_page.create_order()
        main_page.close_order_modal()
        main_page.click_a_order_list()
        assert orders_list_page.get_orders_count_all() == count_before_order + 1

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_order_count_today(self, login, main_page, orders_list_page):
        main_page.click_a_order_list()
        count_before_order = orders_list_page.get_orders_count_today()
        orders_list_page.click_a_constructor()
        main_page.create_order()
        main_page.close_order_modal()
        main_page.click_a_order_list()
        assert orders_list_page.get_orders_count_today() == count_before_order + 1

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, login, main_page, orders_list_page):
        main_page.append_bun()
        main_page.add_ingredients()
        main_page.wait_modal_close()
        main_page.click_create_order()
        order_number = main_page.get_order_number()
        main_page.wait_modal_close()
        main_page.close_order_modal()
        main_page.click_a_order_list()
        assert orders_list_page.find_order_number_in_work(order_number) == int(order_number)
