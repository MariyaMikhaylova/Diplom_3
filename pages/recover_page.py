from locators.recover_page_locators import RecoverPageLocators
from pages.base_page import BasePage


class RecoverPage(BasePage):

    def enter_email(self, user_data):
        self.wait_and_find_element(RecoverPageLocators.EMAIL).send_keys(user_data['email'])

    def click_recover_button(self):
        self.wait_and_find_element(RecoverPageLocators.BUTTON_RECOVER).click()
        self.wait_modal_close()
