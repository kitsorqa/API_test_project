class UserEndpoints:
    def __init__(self):
        self._get_user_by_username = "https://petstore.swagger.io/v2/user/"
        self._get_logs_user_into_system = "https://petstore.swagger.io/v2/user/login"
        self._get_logs_out_current_session = "https://petstore.swagger.io/v2/user/logout"
        self._delete_user = "https://petstore.swagger.io/v2/user/"
        self._update_user = "https://petstore.swagger.io/v2/user/"
        self._create_user = "https://petstore.swagger.io/v2/user"
        self._create_array_of_users = "https://petstore.swagger.io/v2/user/createWithArray"
        self._create_list_of_users = "https://petstore.swagger.io/v2/user/createWithList"