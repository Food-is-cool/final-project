from django.contrib.auth.models import User, Group
from customers.models import CustomerProfile
from rest_framework import serializers
from mainsite.serializers import UserSerializer
from trucks.models import TruckProfile


class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    is_truck = serializers.NullBooleanField(default=False),

    class Meta:
        model = CustomerProfile
        fields = '__all__'

class CustomerUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    customer_profile = CustomerProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'customer_profile',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LikedTruckSerializer(serializers.Serializer):
    truck_id = serializers.IntegerField(read_only=True)
    liked = serializers.NullBooleanField(read_only=True)

    def update(self, instance, validated_data):
        if validated_data['liked']==True:
            truck = TruckProfile.objects.get(id=validated_data['truck_id'])
            instance.customer_profile.liked_trucks.add(truck)
            instance.customer_profile.save()
            return instance

        elif validated_data['liked'] == False:
            truck = TruckProfile.objects.get(id=validated_data['truck_id'])
            instance.customer_profile.liked_trucks.remove(truck)
            instance.customer_profile.save()
            return instance


