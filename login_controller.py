from dataprovider import UserDataProvider


class LoginController:
    # Singleton pattern
    __login_controller = None  # Kjo është variabla e saktë për Singleton
    __logged_in_user = None

    @staticmethod
    def login_user(username, password):
        user_data_provider = UserDataProvider()
        user_list = user_data_provider.user_list
        for user in user_list:
            if user.username == username and user.password == password:
                LoginController.get_instance().__logged_in_user = user
                return True
        return False

    @staticmethod
    def get_instance():
        if LoginController.__login_controller is None:  # Përdor variablën e saktë
            LoginController.__login_controller = LoginController()
        return LoginController.__login_controller

    @staticmethod
    def get_logged_in_user():
        return LoginController.get_instance().__logged_in_user

    @staticmethod
    def is_string_none_or_blank(string):
        # Përmirësimi për të trajtuar boshllëqet
        return string is None or string.strip() == ""
