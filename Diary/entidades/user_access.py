class Access:
    def __init__(self, email, user_type, password):
        self.__email = email
        self.__user_type = user_type
        self.__password = password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def user_type(self):
        return self.__user_type

    @user_type.setter
    def user_type(self, user_type):
        self.__user_type = user_type
