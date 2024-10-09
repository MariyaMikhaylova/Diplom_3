class URLS:
    BURGER_MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
    RECOVER_PASSWORD_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password'
    CREATE_USER_ENDPOINT = '/api/auth/register'
    DELETE_USER_ENDPOINT = '/api/auth/user'
    RESET_PASSWORD_PAGE = 'https://stellarburgers.nomoreparties.site/reset-password'
    PROFILE_PAGE = 'https://stellarburgers.nomoreparties.site/account/profile'
    ORDER_HISTORY_PAGE = 'https://stellarburgers.nomoreparties.site/account/order-history'
    ORDER_LIST_PAGE = 'https://stellarburgers.nomoreparties.site/feed'


class TestUserData:

    USER_DATA = {
        "email": "",
        "password": "",
        "name": ""
    }

    REGISTRATION_USER_BODY = {
        "email": "",
        "password": "",
        "name": ""
    }
