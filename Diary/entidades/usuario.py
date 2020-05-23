class Usuario():

    def __init__(self,
         company_user_name,
         password,
         company_user_cnpj,
         company_user_responsible,
         company_user_contact,
         company_user_email,
         company_user_address_street,
         company_user_address_number,
         company_user_address_cod,
         company_user_address_city,
         company_user_address_state):

        self.__company_user_name = company_user_name
        self.__password = password
        self.__company_user_cnpj = company_user_cnpj
        self.__company_user_responsible = company_user_responsible
        self.__company_user_contact = company_user_contact
        self.__company_user_email = company_user_email
        self.__company_user_address_street = company_user_address_street
        self.__company_user_address_number = company_user_address_number
        self.__company_user_address_cod = company_user_address_cod
        self.__company_user_address_city = company_user_address_city
        self.__company_user_address_state = company_user_address_state

####################################################
    @property
    def company_user_name(self):
        return self.__company_user_name
    @company_user_name.setter
    def company_user_name(self, company_user_name):
        self.__company_user_name = company_user_name
####################################################
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
####################################################
    @property
    def company_user_cnpj(self):
        return self.__company_user_cnpj
    @company_user_cnpj.setter
    def company_user_cnpj(self, company_user_cnpj):
        self.__company_user_cnpj = company_user_cnpj
##################################################
    @property
    def company_user_responsible(self):
        return self.__company_user_responsible
    @company_user_responsible.setter
    def company_user_responsible(self, company_user_responsible):
        self.__company_user_responsible = company_user_responsible
##################################################
    @property
    def company_user_contact(self):
        return self.__company_user_contact
    @company_user_contact.setter
    def company_user_contact(self, company_user_contact):
        self.__company_user_contact = company_user_contact
###################################################
    @property
    def company_user_email(self):
        return self.__company_user_email
    @company_user_email.setter
    def company_user_email(self, company_user_email):
        self.__company_user_email = company_user_email
##################################################
    @property
    def company_user_address_street(self):
        return self.__company_user_address_street
    @company_user_address_street.setter
    def company_user_address_street(self, company_user_address_street):
        self.__company_user_address_street = company_user_address_street
####################################################
    @property
    def company_user_address_number(self):
        return self.__company_user_address_number
    @company_user_address_number.setter
    def company_user_address_number(self, company_user_address_number):
        self.__company_user_address_number = company_user_address_number
#####################################################
    @property
    def company_user_address_cod(self):
        return self.__company_user_address_cod
    @company_user_address_cod.setter
    def company_user_address_cod(self, company_user_address_cod):
        self.__company_user_address_cod = company_user_address_cod
#####################################################
    @property
    def company_user_address_city(self):
        return self.__company_user_address_city
    @company_user_address_city.setter
    def company_user_address_city(self, company_user_address_city):
        self.__company_user_address_city = company_user_address_city
####################################################
    @property
    def company_user_address_state(self):
        return self.__company_user_address_state
    @company_user_address_state.setter
    def company_user_address_state(self, company_user_address_state):
        self.__company_user_address_state = company_user_address_state
####################################################