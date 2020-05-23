class Customer:
    def __init__(self, user_access, customer_name):
        self.__user_access = user_access
        self.__customer_name = customer_name

    @property
    def user_access(self):
        return self.__user_access

    @user_access.setter
    def user_access(self, user_access):
        self.__user_access = user_access

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        self.__customer_name = customer_name
