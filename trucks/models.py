from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from django.db import models
# from mainsite.models import Profile
from mainsite.models import Profile


@receiver(post_save, sender=Profile)
def create_truck_profile(sender, instance=None, created=False, **kwargs):
    if instance.is_truck == True:
        TruckProfile.objects.create(profile=instance)


class TruckProfile(models.Model):
    profile = models.OneToOneField(Profile, related_name='truck_profile')
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



# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def create_truck_profile(sender, instance=None, created=False, **kwargs):
#     Group.objects.get(name='trucks')
#     if created:
#         TruckProfile.objects.create(user=instance)

        # instance.groups.filter(Group.objects.get(name='trucks'))
        # TruckProfile.objects.create(user=instance)

# if instance.groups.filter(name='trucks').exists():
#     TruckProfile.objects.create(user=instance)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_truck_profile(sender, instance=None, created=False, **kwargs):
#     if created:
#         if instance.groups.filter(name='trucks').exists():
#             TruckProfile.objects.create(user=instance)
#         else:
#             CustomerProfile.objects.create(user=instance)


