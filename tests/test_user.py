from services.User.api_user import ApiUser

api_user = ApiUser()


class TestApiUser:

    def test_create_new_user(self):
        api_user.create_new_user()

    def test_user_login_into_system(self):
        api_user.user_login()

    def test_user_logout_from_system(self):
        api_user.user_logout()

    def test_get_user_info_by_username(self):
        api_user.get_user_by_username()

    def test_delete_user_by_username(self):
        api_user.delete_user_by_username('mary73')

    def test_change_user_info_by_username(self):
        api_user.change_user_info_by_username()

    def test_create_users_by_array(self):
        api_user.create_users_by_array(2)

    def test_create_users_by_list(self):
        api_user.create_users_by_array(3)