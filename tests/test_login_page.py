import allure

from data import URLS
from locators.recover_page_locators import RecoverPageLocators
from locators.reset_password_locators import ResetPasswordLocators


class TestLoginPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по клику на гиперссылку "Восстановить пароль"')
    def test_open_recover_password_page(self, login_page, open_login_page):
        login_page.wait_modal_close()
        login_page.click_recover_password()
        login_page.wait_and_find_element(RecoverPageLocators.BUTTON_RECOVER)
        assert login_page.current_url == URLS.RECOVER_PASSWORD_PAGE

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    def test_enter_email_click_recover(self, recover_page, user_data, user_registration, open_recover_page):
        recover_page.enter_email(user_data)
        recover_page.click_recover_button()
        recover_page.wait_and_find_element(ResetPasswordLocators.BUTTON_SAVE)
        assert recover_page.current_url == URLS.RESET_PASSWORD_PAGE

    @allure.title('Проверка отображения пароля')
    def test_show_hide_password(self, recover_page, open_recover_page, reset_page):
        recover_page.click_recover_button()
        reset_page.wait_modal_close()
        reset_page.click_show_password_button()
        assert reset_page.wait_and_find_element(ResetPasswordLocators.SHOW_PASSWORD)

    @allure.title('Проверка клика по ссылке Конструктор')
    def test_click_button_constructor(self, login_page, open_login_page):
        login_page.click_button_constructor()
        login_page.wait_modal_close()
        assert login_page.current_url == URLS.BURGER_MAIN_PAGE
