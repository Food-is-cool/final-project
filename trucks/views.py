import os

from django.contrib.auth.mixins import LoginRequiredMixin
from customers.models import CustomerProfile
from mainsite.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from trucks.models import TruckProfile
from trucks.serializers import TruckProfileSerializer, TruckUserSerializer

class ListCreateTruckUser(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class = TruckUserSerializer

    def perform_create(self, serializer):
        serializer.save()
        user = serializer.instance
        g = Group.objects.get(name='trucks')
        g.user_set.add(user)
        TruckProfile.objects.create(user=user)

class DetailCurrentTruckUser(generics.ListAPIView):
    serializer_class = TruckUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class ListCreateTruckProfile(generics.ListCreateAPIView):
    serializer_class = TruckProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return TruckProfile.objects.all()

class DetailCurrentTruck(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = TruckProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return TruckProfile.objects.filter(user=self.request.user)

# class DetailCurrentTruck(generics.ListAPIView):
#     serializer_class = TruckProfileSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def get_queryset(self):
#         return TruckProfile.objects.filter(id=self.request.user.id)

class DetailUpdateDeleteTruckProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = TruckProfile.objects.all()
    serializer_class = TruckProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # TODO: change this ^ back to IsOwnerOrReadOnly