from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def click_recover_password(self):
        self.wait_and_find_element(LoginPageLocators.RECOVER_PASSWORD).click()

    def enter_email(self, user_data):
        self.wait_and_find_element(LoginPageLocators.EMAIL).send_keys(user_data['email'])

    def enter_password(self, user_data):
        self.wait_and_find_element(LoginPageLocators.PASSWORD).send_keys(user_data['password'])

    def click_button_enter(self):
        self.wait_and_find_element(LoginPageLocators.BUTTON_ENTER).click()

    def click_button_constructor(self):
        self.wait_modal_close()
        self.wait_and_find_element(LoginPageLocators.A_CONSTRUCTOR).click()
