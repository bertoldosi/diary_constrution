class Customer:
    def __init__(self,
                 user_access,
                 engineer,
                 customer_name,
                 customer_cnpj,
                 customer_contact,
                 customer_street,
                 customer_number,
                 customer_city,
                 customer_state,
                 customer_cod,
                 ):
        self.__user_access = user_access
        self.__engineer = engineer
        self.__customer_name = customer_name
        self.__customer_cnpj = customer_cnpj
        self.__customer_contact = customer_contact
        self.__customer_street = customer_street
        self.__customer_street = customer_state
        self.__customer_number = customer_number
        self.__customer_city = customer_city
        self.__customer_state = customer_state
        self.__customer_cod = customer_cod

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

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def engineer(self):
        return self.__engineer

    @engineer.setter
    def engineer(self, engineer):
        self.__engineer = engineer

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def customer_cnpj(self):
        return self.__customer_cnpj

    @customer_cnpj.setter
    def customer_cnpj(self, customer_cnpj):
        self.__customer_cnpj = customer_cnpj

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def customer_contact(self):
        return self.__customer_contact

    @customer_contact.setter
    def customer_contact(self, customer_contact):
        self.__customer_contact = customer_contact

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def customer_street(self):
        return self.__customer_street

    @customer_street.setter
    def customer_street(self, customer_street):
        self.__customer_street = customer_street

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def customer_number(self):
        return self.__customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        self.__customer_number = customer_number

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def customer_city(self):
        return self.__customer_city

    @customer_city.setter
    def customer_city(self, customer_city):
        self.__customer_city = customer_city

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def customer_state(self):
        return self.__customer_state

    @customer_state.setter
    def customer_state(self, customer_state):
        self.__customer_state = customer_state

    # ----------------------------------------------------------------------------------------------------------------
    @property
    def customer_cod(self):
        return self.__customer_cod

    @customer_cod.setter
    def customer_cod(self, customer_cod):
        self.__customer_cod = customer_cod
