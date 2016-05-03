from django.conf import settings
from django.contrib.auth.models import User, Group

from customers.models import CustomerProfile
from mainsite.serializers import UserSerializer
from trucks.models import TruckProfile
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class TruckProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)


    class Meta:
        model = TruckProfile
        fields = '__all__'


