from django.contrib import admin
from trucks.models import TruckProfile


@admin.register(TruckProfile)
class TruckProfileAdmin(admin.ModelAdmin):
    list_display = ('id','truck_name')
