import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from seletools.actions import drag_and_drop

from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def wait_close_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 10).until_not(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @property
    def current_url(self):
        return self.driver.current_url

    def drag_and_drop(self, source, target):
        drag_and_drop(self.driver, source, target)

    def scroll_page(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_modal_close(self):
        self.wait_close_element(MainPageLocators.MODAL)
        time.sleep(1)
