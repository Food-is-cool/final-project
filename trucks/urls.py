from django.conf.urls import url
from trucks.views import DetailCurrentTruck,\
    ListCreateTruckProfile, DetailUpdateDeleteTruckProfile

urlpatterns = [
    url(r'^current/$', DetailCurrentTruck.as_view(),
        name='api_current_truck'),
    url(r'^(?P<pk>\d+)$', DetailUpdateDeleteTruckProfile.as_view(),
        name='api_truckprofile_detail_update'),
    url(r'^$', ListCreateTruckProfile.as_view(),
        name='api_truckprofile_list_create')
]