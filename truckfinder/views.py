import os
from truckfinder.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from truckfinder.models import TruckProfile, CustomerProfile, Address
from rest_framework import generics
from truckfinder.serializers import UserSerializer, TruckProfileSerializer, \
    CustomerProfileSerializer
from django.shortcuts import render

# Create your views here.

class ListCreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class= UserSerializer

class DetailCurrentUser(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    # def get_queryset(self):
    #     user = self.request.user
    #     return user

# class ListCreateProfile(generics.ListCreateAPIView):
#     serializer_class = ProfileSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#     def get_queryset(self):
#         return Profile.objects.filter(user=self.request.user)
#
# class DetailUpdateDeleteProfile(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = (IsOwnerOrReadOnly,)

class ListCreateTruckProfile(generics.ListCreateAPIView):
    serializer_class = TruckProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return TruckProfile.objects.all()

class DetailCurrentTruck(generics.ListAPIView):
    serializer_class = TruckProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        return TruckProfile.objects.filter(user=self.request.user)

class DetailUpdateDeleteTruckProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = TruckProfile.objects.all()
    serializer_class = TruckProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ListCreateCustomerProfile(generics.ListCreateAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return CustomerProfile.objects.all()

class DetailCurrentCustomer(generics.ListAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return CustomerProfile.objects.filter(user=self.request.user)

class DetailUpdateDeleteCustomerProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)