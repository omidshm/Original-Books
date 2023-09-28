#from django.contrib.auth import get_user_model
from store.models import Customer
from datetime import date

# Create a few dummy AppUser instances


# Create Customer instances associated with the dummy AppUser instances
user_id_list = [12,13,14,15,16]
for i in range(5):
    customer = Customer(
        birth_date=date(1990, i, 15),
        user=user_id_list[i],
        phone=f'123{i}'
    )
    customer.save()