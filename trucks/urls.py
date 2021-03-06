from django.conf.urls import url
from trucks.views import ListCreateTruckUser, ListCreateTruckProfile, \
    DetailUpdateDeleteTruckProfile,DetailCurrentTruck, GetYelpRating

urlpatterns = [
    url(r'^users/$', ListCreateTruckUser.as_view(),
        name='api_listcreate_truckuser'),
    url(r'^users/current/$', DetailCurrentTruck.as_view(),
        name='api_current_truck'),
    url(r'^users/yelp/(?P<truck_id>\d+)', GetYelpRating.as_view(),
        name='api_yelp_rating'),
    url(r'^users/(?P<pk>\d+)$', DetailUpdateDeleteTruckProfile.as_view(),
        name='api_truckprofile_detail_update'),
    url(r'^$', ListCreateTruckProfile.as_view(),
        name='api_truckprofile_list_create')

]