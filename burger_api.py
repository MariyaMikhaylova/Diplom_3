from helper import TestDataHelper

class BurgerApi:

    @staticmethod
    def create_user():
        registration_body = TestDataHelper.create_registration_body()
        registration_response = TestDataHelper.create_user(registration_body)
        return registration_response
