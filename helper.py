import random

import requests

from data import URLS, TestUserData


class TestDataHelper:

    def generate_email(length):
        email = ""
        for i in range(length):
            email = email + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwz'))
        return f'{email}@test.br'

    def generate_password(length):
        password = ""
        for i in range(length):
            password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        return password

    def generate_name(length):
        name = ""
        for i in range(length):
            name = name + random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        return name

    @classmethod
    def create_registration_body(cls):
        body = TestUserData.REGISTRATION_USER_BODY.copy()
        body['email'] = TestDataHelper.generate_email(7)
        body['password'] = TestDataHelper.generate_password(7)
        body['name'] = TestDataHelper.generate_name(7)
        return body

    @classmethod
    def create_user(cls, body):
        return requests.post(URLS.BURGER_MAIN_PAGE + URLS.CREATE_USER_ENDPOINT, json=body)

    @staticmethod
    def delete_user(user_token):
        headers = {'Authorization': user_token}
        response_delete = requests.delete(URLS.BURGER_MAIN_PAGE + URLS.DELETE_USER_ENDPOINT, headers=headers)
        return response_delete
