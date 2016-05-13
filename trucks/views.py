from django.contrib.auth.models import User, Group
# from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from yelpapi import YelpAPI
from trucks.models import TruckProfile
from trucks.serializers import TruckProfileSerializer, TruckUserSerializer
# from yelp.client import Client
# from yelp.oauth1_authenticator import Oauth1Authenticator
from yelpapi import YelpAPI


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

class DetailCurrentTruck(generics.ListAPIView):
    serializer_class = TruckProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return TruckProfile.objects.filter(user=self.request.user)

class DetailUpdateDeleteTruckProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = TruckProfile.objects.all()
    serializer_class = TruckProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # TODO: change this ^ back to IsOwnerOrReadOnly


class GetYelpRating(APIView):
    yelp_api = YelpAPI(
            consumer_key='4WE4WWqdHYTVcoBcVWSl1w',
            consumer_secret='3ODmkPnLtpg4mfBF4EquRRY2Fgc',
            token='A2RpqlpG-LGIYWLv8HRvn--idjrobz6_',
            token_secret='e28huvUknMW-4eaEGTFrRt7PHlM'
            )

    def get(self, request, truck_id, format=None):
        truck = TruckProfile.objects.get(id=truck_id)
        id = truck.biz_id_yelp
        response = self.yelp_api.business_query(id=id)
        return Response(response)





# def get(self, request, format=None):
        # client = Client(auth)
        # # id = TruckProfile.biz_id_yelp
        #
        # return client.get_business('yelp-san-francisco')



# def get(self, request, format=None):
#
#     # return HttpResponse('ok')
#
#     params = {
#         'lang': 'fr'
#     }
#
#         client.get_business('yelp-san-francisco', **params)



    # def get_queryset(self):
    #     return TruckProfile.objects.filter(user=self.request.user)
    #
    # def get(self, format=None):
    #     x = self.request.user.truckprofile.yelp_biz_id
    #     result = 'https://api.yelp.com/v2/business/{}?actionlinks=True'.format(TruckProfile.yelp_biz_id)
    #     return result


# class DetailCurrentTruck(generics.ListAPIView):
#     serializer_class = TruckProfileSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def get_queryset(self):
#         return TruckProfile.objects.filter(id=self.request.user.id)
