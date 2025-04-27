import logging

import requests

from services.User.endpoints import UserEndpoints
from services.User.models.model_User import ResponseUser, ResponseUserByUsername
from services.User.payloads import UserPayloads
from config.headers import Headers

custom_headers = Headers()

class ApiUser:
    def __init__(self):
        self._endpoints = UserEndpoints()
        self._payloads = UserPayloads()

    def create_new_user(self):
        response = requests.post(
            url=self._endpoints._create_user,
            json=self._payloads.create_user()
        )
        logging.info(response.json())
        model = ResponseUser(**response.json())
        return model

    def user_login(self):
        response = requests.get(
            url=self._endpoints._get_logs_user_into_system,
            params={"username": "test", "password": "test"},
        )
        logging.info(response.text)
        model = ResponseUser(**response.json())
        return model

    def user_logout(self):
        response = requests.get(
            url=self._endpoints._get_logs_user_into_system,
            params={"username": "test", "password": "test"},
        )
        logging.info(response.text)
        model = ResponseUser(**response.json())
        return model

    def get_user_by_username(self, username='test'):
        response = requests.get(
            url=f"{self._endpoints._get_user_by_username}{username}",
        )
        if response.status_code == 200:
            model = ResponseUserByUsername(**response.json())
            return model
        else:
            model = ResponseUser(**response.json())
            return model

    def delete_user_by_username(self, username='test'):
        response = requests.delete(
            url=f"{self._endpoints._delete_user}{username}"
        )
        if response.status_code == 200:
            model = ResponseUser(**response.json())
            return model
        raise TypeError("Пользователь с таким никнеймом не найден")

    def change_user_info_by_username(self, username='mary73'):
        response = requests.put(
            url=f"{self._endpoints._update_user}{username}",
            json=self._payloads.change_user()
        )
        model = ResponseUser(**response.json())
        return model

    def create_users_by_array(self, count_of_users):
        response = requests.post(
            url=f"{self._endpoints._create_array_of_users}",
            json=self._payloads.create_array_of_users(count_of_users),
            headers=custom_headers.headers
        )
        model = ResponseUser(**response.json())
        return model

    def create_users_by_list(self, count_of_users):
        response = requests.post(
            url=f"{self._endpoints._create_list_of_users}",
            json=self._payloads.create_array_of_users(count_of_users),
            headers=custom_headers.headers
        )
        model = ResponseUser(**response.json())
        return model