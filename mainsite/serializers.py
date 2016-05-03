from rest_framework import serializers
from django.contrib.auth.models import User, Group
from customers.models import CustomerProfile
from mainsite import models
from trucks.models import TruckProfile


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

# class ProfileSerializer(serializers.ModelSerializer):
#     is_truck = serializers.NullBooleanField(default=None)
#
#     class Meta:
#         model = Profile
#         fields = ('id', 'user', 'is_truck',)

    # def create(self, validated_data):
    #     profiles_data = validated_data.pop('profile_set')
    #     is_truck = models.Profile.objects.create(**validated_data)
    #     for profile in profiles_data:
    #         models.Profile.objects.create(is_truck=is_truck, **profile)
    #     is_truck.save()
    #     return is_truck

    # def perform_create(self, validated_data):
    #     if validated_data['is_truck']==True:
    #         TruckProfile.objects.create(user=self.request.user)
    #     else:
    #         CustomerProfile.objects.create(user=self.request.user)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    # profile = ProfileSerializer(read_only=True)
    # is_truck = serializers.NullBooleanField(source='profile.is_truck')

    class Meta:
        model = User
        fields = ('id','username', 'password')

    def create(self, validated_data):
        # profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        # Profile.objects.create(user=user, **profile_data)
        return user

