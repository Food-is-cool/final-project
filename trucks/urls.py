from django.conf.urls import url
from trucks.views import DetailCurrentTruck, ListCreateTruckUser,\
    ListCreateTruckProfile, DetailUpdateDeleteTruckProfile

urlpatterns = [
    url(r'^users/$', ListCreateTruckUser.as_view(),
        name='api_createtruck_user'),
    url(r'^users/current/$', DetailCurrentTruck.as_view(),
        name='api_current_truck'),
    url(r'^users/(?P<pk>\d+)$', DetailUpdateDeleteTruckProfile.as_view(),
        name='api_truckprofile_detail_update'),
    url(r'^$', ListCreateTruckProfile.as_view(),
        name='api_truckprofile_list_create')
]