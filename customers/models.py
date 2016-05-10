from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from django.db import models
# from notifications.models import SMSNotifications, EmailBlasts



class CustomerProfile(models.Model):
    user = models.OneToOneField(User, related_name='customer_profile')
    liked_trucks = models.ManyToManyField('trucks.TruckProfile',
                                          blank=True)
    is_truck = models.BooleanField(default=False)
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    want_texts= models.BooleanField(default=False)
    want_emails = models.BooleanField(default=False)
    email_address = models.EmailField(null=True, blank=True)
    # email_address = models.ForeignKey(EmailBlasts, null=True, blank=True)
    mobile_number = models.CharField(max_length=12, null=True, blank=True)
    # text_number = models.ForeignKey(SMSNotifications, null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    suite_number = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)


