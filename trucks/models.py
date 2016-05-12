from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from django.db import models

class TruckProfile(models.Model):
    user = models.OneToOneField(User, related_name='truck_profile')
    is_truck = models.BooleanField(default=True)
    truck_name = models.CharField(max_length=255, null=True, blank=True)
    truck_description = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    expiration = models.DateTimeField(null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    facebook_page = models.URLField(null=True, blank=True)
    twitter_page = models.URLField(null=True, blank=True)
    instagram_page = models.URLField(null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    cuisine = models.CharField(max_length=255, null=True, blank=True)
    specials = models.TextField(null=True, blank=True)
    biz_id_yelp = models.CharField(max_length=250, null=True, blank = True)
    # menu_items = models.TextField(null=True, blank=True)
    menu_item_1 = models.CharField(max_length=255, null=True, blank=True)
    menu_item_2 = models.CharField(max_length=255, null=True, blank=True)
    menu_item_3 = models.CharField(max_length=255, null=True, blank=True)
    menu_item_4 = models.CharField(max_length=255, null=True, blank=True)
    menu_item_5 = models.CharField(max_length=255, null=True, blank=True)
    menu_item_6 = models.CharField(max_length=255, null=True, blank=True)
    menu_item_7 = models.CharField(max_length=255, null=True, blank=True)
    menu_item_8 = models.CharField(max_length=255, null=True, blank=True)
    menu_item_9 = models.CharField(max_length=255, null=True, blank=True)
    menu_item_10 = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.id) + " " + str(self.truck_name)

