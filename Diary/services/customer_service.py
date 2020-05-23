from ..models import Customer


def Register_customer(customer):
    customer = Customer.objects.create(user_access=customer.user_access, customer_name=customer.customer_name)

    customer.save()
