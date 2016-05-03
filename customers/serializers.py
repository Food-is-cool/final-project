from django.contrib.auth.models import User, Group
from customers.models import CustomerProfile
from rest_framework import serializers
from mainsite.serializers import UserSerializer


class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CustomerProfile
        fields = '__all__'

