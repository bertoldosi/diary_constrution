class Engineer:
    def __init__(self, user_access,
                 engineer_name,
                 engineer_cnpj,
                 engineer_contact,
                 engineer_street,
                 engineer_number,
                 engineer_city,
                 engineer_state,
                 engineer_cod
                 ):
        self.__user_access = user_access
        self.__engineer_name = engineer_name
        self.__engineer_cnpj = engineer_cnpj
        self.__engineer_contact = engineer_contact
        self.__engineer_street = engineer_street
        self.__engineer_number = engineer_number
        self.__engineer_city = engineer_city
        self.__engineer_state = engineer_state
        self.__engineer_cod = engineer_cod

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

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def engineer_cnpj(self):
        return self.__engineer_cnpj

    @engineer_cnpj.setter
    def engineer_cnpj(self, engineer_cnpj):
        self.__engineer_cnpj = engineer_cnpj

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def engineer_contact(self):
        return self.__engineer_contact

    @engineer_contact.setter
    def engineer_contact(self, engineer_contact):
        self.__engineer_contact = engineer_contact

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def engineer_street(self):
        return self.__engineer_street

    @engineer_street.setter
    def engineer_street(self, engineer_street):
        self.__engineer_street = engineer_street

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def engineer_number(self):
        return self.__engineer_number

    @engineer_number.setter
    def engineer_number(self, engineer_number):
        self.__engineer_number = engineer_number

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def engineer_city(self):
        return self.__engineer_city

    @engineer_city.setter
    def engineer_city(self, engineer_city):
        self.__engineer_city = engineer_city

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def engineer_state(self):
        return self.__engineer_state

    @engineer_state.setter
    def engineer_state(self, engineer_state):
        self.__engineer_state = engineer_state

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def engineer_cod(self):
        return self.__engineer_cod

    @engineer_cod.setter
    def engineer_cod(self, engineer_cod):
        self.__engineer_cod = engineer_cod