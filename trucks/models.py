from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from django.db import models


class TruckProfile(models.Model):
    user = models.OneToOneField(User, related_name='truck_profile')
    truck_name = models.CharField(max_length=255, null=True, blank=True)
    truck_description = models.TextField(null=True, blank=True)
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
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)




# @receiver(post_save, sender=Profile)
# def create_truck_profile(sender, instance=None, created=False, **kwargs):
#     if instance.is_truck == True:
#         TruckProfile.objects.create(profile=instance)