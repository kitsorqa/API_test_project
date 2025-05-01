import allure
from allure_commons.types import Severity

from services.User.api_user import ApiUser
from utils.attachments import log_api

api_user = ApiUser()


class TestApiUser:

    @allure.title("Создание нового пользователя")
    @allure.tag("api")
    @allure.severity(Severity.CRITICAL)
    def test_create_new_user(self):
        api_user.create_new_user()

    @allure.title("Авторизация пользователя")
    @allure.tag("api")
    @allure.severity(Severity.CRITICAL)
    def test_user_login_into_system(self):
        api_user.user_login()

    @allure.title("Разлогин пользователя")
    @allure.tag("api")
    @allure.severity(Severity.CRITICAL)
    def test_user_logout_from_system(self):
        api_user.user_logout()

    @allure.title("Получение информации о пользователе")
    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    def test_get_user_info_by_username(self):
        api_user.get_user_by_username()

    @allure.title("Удаление пользователя")
    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    def test_delete_user_by_username(self):
        api_user.delete_user_by_username('mary73')

    @allure.title("Изменение данных о пользователе")
    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    def test_change_user_info_by_username(self):
        api_user.change_user_info_by_username()

    @allure.title("Создание новых пользователей, используя массив")
    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    def test_create_users_by_array(self):
        api_user.create_users_by_array(2)

    @allure.title("Создание новых пользователей, используя список")
    @allure.tag("api")
    @allure.severity(Severity.NORMAL)
    def test_create_users_by_list(self):
        api_user.create_users_by_array(3)