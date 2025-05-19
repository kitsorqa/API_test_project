import requests
from allure_commons._allure import step

from services.User.endpoints import UserEndpoints
from services.User.models.model_User import ResponseUser, ResponseUserByUsername
from services.User.payloads import UserPayloads
from config.headers import Headers
from utils.attachments import log_api

custom_headers = Headers()


class ApiUser:
    def __init__(self):
        self._endpoints = UserEndpoints()
        self._payloads = UserPayloads()

    def create_new_user(self):
        with step("Создание пользователя, используя рандомную генерацию из валидных значений"):
            response = requests.post(
                url=self._endpoints._create_user,
                json=self._payloads.create_user()
            )
            log_api(response)
            model = ResponseUser(**response.json())
            return model

    def user_login(self):
        with step("Авторизация пользователя, используя тестовые валидные данные"):
            response = requests.get(
                url=self._endpoints._get_logs_user_into_system,
                params={"username": "test", "password": "test"},
            )
            log_api(response)
            model = ResponseUser(**response.json())
            return model

    def user_logout(self):
        with step("Разлогин пользователя, используя валидные значения"):
            response = requests.get(
                url=self._endpoints._get_logs_user_into_system,
                params={"username": "test", "password": "test"},
            )
            log_api(response)
            model = ResponseUser(**response.json())
            return model

    def get_user_by_username(self, username='test'):
        with step("Получение информации о валидном пользователе по его юзернейму"):
            response = requests.get(
                url=f"{self._endpoints._get_user_by_username}{username}",
            )
            log_api(response)
            if response.status_code == 200:
                with step("Пользователь существует и информация получена"):
                    model = ResponseUserByUsername(**response.json())
                    return model
            with step("Пользователь не существует"):
                model = ResponseUser(**response.json())
                return model

    def delete_user_by_username(self, username='mary73'):
        with step("Удаление валидного пользователя по его юзернейму"):
            response = requests.delete(
                url=f"{self._endpoints._delete_user}{username}"
            )
            log_api(response)
            if response.status_code == 200:
                with step("Пользователь существует и удален"):
                    model = ResponseUser(**response.json())
                    return model
            with step("Пользователь не найден"):
                raise TypeError("Пользователь с таким никнеймом не найден")

    def change_user_info_by_username(self, username='mary73'):
        with step("Изменение данных о пользователе"):
            response = requests.put(
                url=f"{self._endpoints._update_user}{username}",
                json=self._payloads.change_user()
            )
            log_api(response)
            model = ResponseUser(**response.json())
            return model

    def create_users_by_array(self, count_of_users):
        with step("Создание массива пользователей"):
            response = requests.post(
                url=f"{self._endpoints._create_array_of_users}",
                json=self._payloads.create_array_of_users(count_of_users),
                headers=custom_headers.headers
            )
            log_api(response)
            model = ResponseUser(**response.json())
            return model


    def create_users_by_list(self, count_of_users):
        with step("Создание списка пользователей"):
            response = requests.post(
                url=f"{self._endpoints._create_list_of_users}",
                json=self._payloads.create_array_of_users(count_of_users),
                headers=custom_headers.headers
            )
            log_api(response)
            model = ResponseUser(**response.json())
            return model
