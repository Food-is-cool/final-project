from django.contrib.auth.models import User, Group
from customers.models import CustomerProfile
from rest_framework import serializers
from mainsite.serializers import UserSerializer


class CustomerUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = '__all__'

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user

class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CustomerProfile
        fields = '__all__'

