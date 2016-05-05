from rest_framework import serializers
from django.contrib.auth.models import User, Group
from mainsite import models

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    is_truck = serializers.NullBooleanField(source='truck_profile.is_truck')
    is_truck1 = serializers.NullBooleanField(source='customer_profile.is_truck')

    class Meta:
        model = User
        fields = ('id','username', 'password', 'is_truck', 'is_truck1')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

