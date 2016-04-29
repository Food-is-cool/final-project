from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include
from truckfinder.views import ListCreateUser, DetailUpdateDeleteTruckProfile, \
    ListCreateTruckProfile, DetailUpdateDeleteCustomerProfile, \
    ListCreateCustomerProfile, DetailUpdateDeleteProfile, ListCreateProfile

urlpatterns = [
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^users/$', ListCreateUser.as_view(),
        name='api_user_list_create'),
    url(r'^profiles/(?P<pk>\d+)$', DetailUpdateDeleteProfile.as_view(),
        name='api_profile_detail_update'),
    url(r'^profiles/$', ListCreateProfile.as_view(),
        name='api_profile_list_create'),
    url(r'^trucks/(?P<pk>\d+)$', DetailUpdateDeleteTruckProfile.as_view(),
        name='api_truckprofile_detail_update'),
    url(r'^trucks/$', ListCreateTruckProfile.as_view(),
        name='api_truckprofile_list_create'),
    url(r'^customers/(?P<pk>\d+)$',
        DetailUpdateDeleteCustomerProfile.as_view(),
        name='api_customerprofile_detail_update'),
    url(r'^customers/$', ListCreateCustomerProfile.as_view(),
        name='api_customerprofile_list_create')
]