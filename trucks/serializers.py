from django.contrib.auth.models import User
from mainsite.serializers import UserSerializer
from trucks.models import TruckProfile
from rest_framework import serializers


class TruckProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    is_truck = serializers.NullBooleanField(default=False),

    class Meta:
        model = TruckProfile
        fields = '__all__'


# class TruckLocationSerializer(ser)
# truck id, lat, long

class TruckUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    truck_profile = TruckProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'truck_profile',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user