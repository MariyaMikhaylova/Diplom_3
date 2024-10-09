import allure

from data import URLS
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators


class TestMainPage:

    @allure.title('Проверка перехода на страницу личного кабинета')
    def test_open_profile_page(self, login_page, open_login_page, user_data, user_registration, main_page):
        login_page.enter_email(user_data)
        login_page.enter_password(user_data)
        login_page.click_button_enter()
        main_page.wait_modal_close()
        main_page.click_button_account()
        main_page.wait_and_find_element(ProfilePageLocators.A_PROFILE)
        assert main_page.current_url == URLS.PROFILE_PAGE

    @allure.title('Проверка перехода по клику на ссылку Лента заказов')
    def test_click_a_order_list(self, main_page, open_main_page):
        main_page.wait_modal_close()
        main_page.click_a_order_list()
        assert main_page.current_url == URLS.ORDER_LIST_PAGE

    @allure.title('Проверка открытия модального окна с деталями ингридиента')
    def test_open_modal_ingredient(self, main_page, open_main_page):
        main_page.wait_modal_close()
        main_page.click_crater_bun()
        assert main_page.wait_and_find_element(MainPageLocators.MODAL_INGREDIENT_TITLE).text == "Детали ингредиента"

    @allure.title('Проверка закрытия модального окна с деталями ингридиента')
    def test_close_modal_ingredient(self, main_page, open_main_page):
        main_page.wait_modal_close()
        main_page.click_crater_bun()
        main_page.close_modal_ingredient()
        assert main_page.wait_and_find_element(MainPageLocators.TITLE).text == "Соберите бургер"

    @allure.title('Проверка увеличения каунтера при добавлении булки в бургер')
    def test_close_modal_ingredient(self, main_page, open_main_page):
        main_page.append_bun()
        assert main_page.wait_and_find_element(MainPageLocators.COUNTER_CRATER_BUN).text == "2"

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    def test_open_profile_page(self, login_page, open_login_page, user_data, user_registration, main_page):
        login_page.enter_email(user_data)
        login_page.enter_password(user_data)
        login_page.click_button_enter()
        main_page.wait_modal_close()
        main_page.append_bun()
        main_page.click_create_order()
        main_page.wait_and_find_element(MainPageLocators.TEXT_IDENTITY_ORDER)
        assert int(main_page.wait_and_find_element(MainPageLocators.ORDER_NUMBER).text) > 0
