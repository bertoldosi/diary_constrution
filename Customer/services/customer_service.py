from Diary.models import Customer


def Register_customer(customer):
    customer = Customer.objects.create(user_access=customer.user_access,
                                       engineer=customer.engineer,
                                       customer_name=customer.customer_name,
                                       customer_cnpj=customer.customer_cnpj,
                                       customer_contact=customer.customer_contact,
                                       customer_street=customer.customer_street,
                                       customer_number=customer.customer_number,
                                       customer_city=customer.customer_city,
                                       customer_state=customer.customer_state,
                                       customer_cod=customer.customer_cod,
                                       )
    customer.save()
