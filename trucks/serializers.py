from django.conf import settings
from django.contrib.auth.models import User
from mainsite.serializers import UserSerializer
from trucks.models import TruckProfile
from rest_framework import serializers


class TruckUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TruckProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TruckProfile
        fields = '__all__'