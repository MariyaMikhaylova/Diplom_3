from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    def click_a_order_history(self):
        self.wait_and_find_element(ProfilePageLocators.A_HISTORY).click()

    def click_button_exit(self):
        self.wait_and_find_element(ProfilePageLocators.BUTTON_EXIT).click()
