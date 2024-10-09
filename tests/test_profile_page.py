import allure

from data import URLS
from locators.login_page_locators import LoginPageLocators


class TestProfilePage:

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_open_order_history(self, login_open_profile_page, profile_page):
        profile_page.wait_modal_close()
        profile_page.click_a_order_history()
        profile_page.wait_modal_close()
        assert profile_page.current_url == URLS.ORDER_HISTORY_PAGE

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, login_open_profile_page, profile_page):
        profile_page.click_button_exit()
        profile_page.wait_modal_close()
        profile_page.wait_and_find_element(LoginPageLocators.EMAIL)
        assert profile_page.current_url == URLS.LOGIN_PAGE
