from django.contrib import admin
from truckfinder.models import TruckProfile, CustomerProfile #,   Address


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'is_truck')

@admin.register(TruckProfile)
class TruckProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','truck_name')

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'customer_name',
                    'want_texts', 'want_emails',
                    'email_address', 'mobile_number',
                    'street_address', 'city', 'suite_number',
                    'state', 'zipcode')

# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
#     list_display = ('id', 'street_address',
#                     'city', 'suite_number', 'state', 'zipcode')