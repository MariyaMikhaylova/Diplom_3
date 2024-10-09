from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    def click_show_password_button(self):
        self.wait_and_find_element(ResetPasswordLocators.SWG_PASSWORD).click()
