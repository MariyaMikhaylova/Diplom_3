import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_button_account(self):
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10)
                                   .until(EC.element_to_be_clickable(MainPageLocators.BUTTON_ACCOUNT)))

    def click_crater_bun(self):
        self.wait_and_find_element(MainPageLocators.CRATER_BUN).click()

    def close_modal_ingredient(self):
        self.wait_and_find_element(MainPageLocators.MODAL_INGREDIENT_CLOSE).click()

    def append_bun(self):
        source = self.wait_and_find_element(MainPageLocators.CRATER_BUN)
        target = self.wait_and_find_element(MainPageLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop(source, target)

    def click_create_order(self):
        self.wait_and_find_element(MainPageLocators.BUTTON_CREATE_ORDER).click()

    def close_order_modal(self):
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10)
                                   .until(EC.element_to_be_clickable(MainPageLocators.CLOSE_ORDER_BUTTON)))
        self.wait_close_element(MainPageLocators.ORDER_MODAL)

    def get_order_number(self):
        time.sleep(5)
        return self.wait_and_find_element(MainPageLocators.ORDER_NUMBER).text

    def click_a_order_list(self):
        self.wait_modal_close()
        self.wait_and_find_element(MainPageLocators.A_ORDERS_LIST).click()

    def create_order(self):
        self.wait_modal_close()
        self.append_bun()
        self.wait_and_find_element(MainPageLocators.BUTTON_CREATE_ORDER).click()

    def add_ingredients(self):
        target = self.wait_and_find_element(MainPageLocators.BURGER_CONSTRUCTOR)
        ingredient_1 = self.wait_and_find_element(MainPageLocators.SPACE_SAUSE)
        self.scroll_page(ingredient_1)
        self.drag_and_drop(ingredient_1, target)
        ingredient_2 = self.wait_and_find_element(MainPageLocators.FILE_LUM_T)
        self.scroll_page(ingredient_2)
        self.drag_and_drop(ingredient_2, target)
        ingredient_3 = self.wait_and_find_element(MainPageLocators.FALL_TREE)
        self.scroll_page(ingredient_3)
        self.drag_and_drop(ingredient_3, target)
