from django.db import models

#  Create your models here.

# need to add a directory class when I want to give users the option of
# having more than one mobile number and email address.
from customers.models import CustomerProfile

#via Twilio
class SMSNotifications(models.Model):
    text_content = models.TextField(max_length=160, null=True, blank=True)
    media_url = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)

    # def __str__(self):
    #     return self.
# via Sendgrid

class EmailBlasts(models.Model):
    to_email = models.CharField(max_length=255, null=True, blank=True)
    from_email = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.to_email
