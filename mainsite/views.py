from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from mainsite.serializers import UserSerializer, GroupSerializer


# ================   User Views ==================== #

class DetailUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class= UserSerializer

class DetailCurrentUser(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

# =================  Group View ==================== #

class ListGroups(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
