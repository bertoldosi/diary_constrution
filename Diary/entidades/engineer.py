class Engineer:
    def __init__(self, user_access, engineer_name):
        self.__user_access = user_access
        self.__engineer_name = engineer_name

    @property
    def user_access(self):
        return self.__user_access

    @user_access.setter
    def user_access(self, user_access):
        self.__user_access = user_access

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def engineer_name(self):
        return self.__engineer_name

    @engineer_name.setter
    def engineer_name(self, engineer_name):
        self.__engineer_name = engineer_name
