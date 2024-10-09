import pytest
from selenium import webdriver

from data import URLS, TestUserData
from helper import TestDataHelper
from locators.profile_page_locators import ProfilePageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.orders_list_page import OrderListPage
from pages.profile_page import ProfilePage
from pages.recover_page import RecoverPage
from pages.reset_password_page import ResetPasswordPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.get(URLS.BURGER_MAIN_PAGE)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page


@pytest.fixture(scope='function')
def open_login_page(login_page):
    login_page.open_page(URLS.LOGIN_PAGE)


@pytest.fixture(scope='function')
def recover_page(driver):
    recover_page = RecoverPage(driver)
    return recover_page


@pytest.fixture(scope='function')
def open_recover_page(recover_page):
    recover_page.open_page(URLS.RECOVER_PASSWORD_PAGE)
    recover_page.wait_modal_close()


@pytest.fixture(scope='function')
def user_registration(user_data):
    registration_body = TestUserData.REGISTRATION_USER_BODY.copy()
    registration_body['email'] = user_data['email']
    registration_body['name'] = user_data['name']
    registration_body['password'] = user_data['password']
    registration_response = TestDataHelper.create_user(registration_body)
    yield registration_response
    TestDataHelper.delete_user(registration_response.json()['accessToken'])


@pytest.fixture(scope='function')
def user_data():
    data = TestUserData.USER_DATA.copy()
    data['email'] = TestDataHelper.generate_email(7)
    data['password'] = TestDataHelper.generate_password(7)
    data['name'] = TestDataHelper.generate_name(7)
    return data


@pytest.fixture(scope='function')
def reset_page(driver):
    reset_page = ResetPasswordPage(driver)
    return reset_page


@pytest.fixture(scope='function')
def main_page(driver):
    main_page = MainPage(driver)
    return main_page


@pytest.fixture(scope='function')
def open_main_page(main_page):
    main_page.open_page(URLS.BURGER_MAIN_PAGE)


@pytest.fixture(scope='function')
def profile_page(driver):
    profile_page = ProfilePage(driver)
    return profile_page


@pytest.fixture(scope='function')
def login_open_profile_page(login_page, open_login_page, user_data, user_registration, main_page):
    login_page.enter_email(user_data)
    login_page.enter_password(user_data)
    login_page.click_button_enter()
    main_page.wait_modal_close()
    main_page.click_button_account()
    main_page.wait_modal_close()
    main_page.wait_and_find_element(ProfilePageLocators.A_PROFILE)


@pytest.fixture(scope='function')
def login_and_create_order(login_page, open_login_page, user_data, user_registration, main_page):
    login_page.enter_email(user_data)
    login_page.enter_password(user_data)
    login_page.click_button_enter()
    main_page.wait_modal_close()
    main_page.append_bun()
    main_page.click_create_order()


@pytest.fixture(scope='function')
def order_history_page(driver):
    order_history_page = OrderHistoryPage(driver)
    return order_history_page


@pytest.fixture(scope='function')
def orders_list_page(driver):
    orders_list_page = OrderListPage(driver)
    return orders_list_page


@pytest.fixture(scope='function')
def login(login_page, open_login_page, user_data, user_registration):
    login_page.enter_email(user_data)
    login_page.enter_password(user_data)
    login_page.click_button_enter()
    login_page.wait_modal_close()
