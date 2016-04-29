from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

#

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        if instance.is_staff:
            TruckProfile.objects.create(user=instance)
        else:
            CustomerProfile.objects.create(user=instance)


# @receiver(post_save)
# def create_type_profile(self, **kwargs):
#     if self.is_truck == True:
#         TruckProfile.objects.create()
#     if self.is_truck == False:
#         CustomerProfile.objects.create()

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True,
#                                 related_name='profile')
#     is_truck = models.CharField(max_length=3, null=True)

class TruckProfile(models.Model):
    user = models.OneToOneField(User, related_name='truck_profile')
    truck_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=12)
    website = models.URLField()
    facebook_page = models.URLField()
    twitter_page = models.URLField()
    instagram_page = models.URLField()
    logo_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

# class TruckLocation(models.Model):

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, related_name='customer_profile')
    customer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    want_texts= models.BooleanField(default=False)
    want_emails = models.BooleanField(default=False)
    email_address = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    # evening_address
    # weekend_address

class Address(models.Model):
    customer_profile = models.ForeignKey(CustomerProfile, related_name='address')
    truck_profile = models.ForeignKey(TruckProfile, related_name='address')
    street_number = models.TextField()
    city = models.TextField()
    suite_number = models.TextField(null=True)
    state = models.TextField()
    zipcode = models.TextField()
