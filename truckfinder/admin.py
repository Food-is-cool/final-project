from django.contrib import admin
from truckfinder.models import TruckProfile, CustomerProfile, Address, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_truck')

@admin.register(TruckProfile)
class TruckProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile','truck_name', 'created_at', 'modified_at')

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'customer_name',
                    'created_at', 'modified_at', 'want_texts', 'want_emails',
                    'email_address', 'mobile_number')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_profile', 'truck_profile', 'street_number',
                    'city', 'suite_number', 'state', 'zipcode')

