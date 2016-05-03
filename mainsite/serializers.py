from rest_framework import serializers
from django.contrib.auth.models import User, Group
from customers.models import CustomerProfile
from mainsite.models import Profile
from trucks.models import TruckProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    is_truck = serializers.BooleanField(write_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    # def perform_create(self, validated_data):
    #     if validated_data['is_truck']==True:
    #         TruckProfile.objects.create(user=self.request.user)
    #     else:
    #         CustomerProfile.objects.create(user=self.request.user)







# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=128, write_only=True)
#     # category = serializers.CharField(max_length=10, read_only=True)
#     # is_staff = serializers.BooleanField(read_only=True)
#
#     class Meta:
#         model = User
#         fields = '__all__'
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         if validated_data['category'] == 'trucks':
#             TruckProfile.objects.create(user=user)
#         else:
#             CustomerProfile.objects.create(user=user)
#         return user
