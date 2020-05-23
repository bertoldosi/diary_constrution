class User():
    def __init__(self, user_access, user_name, user_type):
        self.__user_access = user_access
        self.__user_name = user_name
        self.__user_type = user_type

    @property
    def user_access(self):
        return self.__user_access

    @user_access.setter
    def user_access(self, user_access):
        self.__user_access = user_access

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def user_type(self):
        return self.__user_type

    @user_type.setter
    def user_type(self, user_type):
        self.__user_type = user_type
    # ----------------------------------------------------------------------------------------------------------------
