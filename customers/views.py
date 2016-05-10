from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User, Group
from customers.models import CustomerProfile
from rest_framework import generics
from customers.serializers import CustomerProfileSerializer, \
    CustomerUserSerializer
from trucks.models import TruckProfile


class CreateCustomerUser(generics.CreateAPIView):
    model = User
    serializer_class = CustomerUserSerializer

    def perform_create(self, serializer):
        serializer.save()
        user = serializer.instance
        g = Group.objects.get(name='customers')
        g.user_set.add(user)
        CustomerProfile.objects.create(user=user)

class DetailCurrentCustomer(generics.ListAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return CustomerProfile.objects.filter(user=self.request.user)

class ListCreateCustomerProfile(generics.ListCreateAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return CustomerProfile.objects.all()

class DetailUpdateDeleteCustomerProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #TODO: change this back to "IsOwnerorReadOnly"

def like_truck(request, truck_id):
    truck = TruckProfile.objects.get(id=truck_id)
    request.user.customer_profile.liked_truck.add(truck)
    return HttpResponse('ok')

def unlike_truck(request, truck_id):
    truck = TruckProfile.objects.get(id=truck_id)
    request.user.customer_profile.liked_truck.remove(truck)
    return HttpResponse('ok')








# class DetailCurrentCustomerUser(generics.ListAPIView):
#     serializer_class = CustomerUserSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def get_queryset(self):
#         return User.objects.filter(id=self.request.user.id)
# class DetailCurrentCustomer(generics.ListAPIView):
#     serializer_class = CustomerProfileSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def get_queryset(self):
#         return CustomerProfile.objects.filter(id=self.request.user.id)