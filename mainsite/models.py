from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from django.db import models


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profiles')
    is_truck = models.NullBooleanField(null=True, blank=True)

    def __str__(self):
        return self.user.username