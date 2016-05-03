from django.contrib import admin
from customers.models import CustomerProfile


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'customer_name',
                    'want_texts', 'want_emails',
                    'email_address', 'mobile_number',
                    'street_address', 'city', 'suite_number',
                    'state', 'zipcode')
