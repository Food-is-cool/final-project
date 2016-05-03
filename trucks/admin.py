from django.contrib import admin
from trucks.models import TruckProfile


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'is_truck')

@admin.register(TruckProfile)
class TruckProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile','truck_name')


# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
#     list_display = ('id', 'street_address',
#                     'city', 'suite_number', 'state', 'zipcode')