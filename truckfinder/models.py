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
    user = models.ForeignKey(User, related_name='truck_profile')
    truck_name = models.CharField(max_length=255, null=True, blank=True)
    truck_description = models.TextField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitutde = models.FloatField(null=True, blank=True)
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
    # address = models.ForeignKey(Address, null=True, blank=True,
                                # related_name='truck_profile')

# class TruckLocation(models.Model):

class CustomerProfile(models.Model):
    user = models.ForeignKey(User, related_name='customer_profile')
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    want_texts= models.BooleanField(default=False)
    want_emails = models.BooleanField(default=False)
    email_address = models.EmailField(null=True, blank=True)
    mobile_number = models.CharField(max_length=12, null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    suite_number = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    # address = models.ForeignKey(Address, null=True, blank=True,
    #                           related_name='customer_profile')

class Address(models.Model):
    # user = models.ForeignKey(User, related_name='address')
    # customer_profile = models.ForeignKey(CustomerProfile,
    #                                      null=True, blank=True,
    #                                      related_name='address')
    # truck_profile = models.ForeignKey(TruckProfile, related_name='address')
    street_address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    suite_number = models.TextField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=2, null=True)
    zipcode = models.CharField(max_length=5, null=True)

    def __unicode__(self):
        return self.street_address

    def __str__(self):
        return self.street_address



