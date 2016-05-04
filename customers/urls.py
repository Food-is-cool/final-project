from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include

from customers.views import DetailUpdateDeleteCustomerProfile, \
    ListCreateCustomerProfile, CreateCustomerUser, DetailCurrentCustomerUser

urlpatterns = [
    url(r'^users/$', CreateCustomerUser.as_view(),
       name='api_createcustomer_user'),
    url(r'^users/current/$', DetailCurrentCustomerUser.as_view(),
        name='api_current_customer'),
    url(r'^users/(?P<pk>\d+)$',
        DetailUpdateDeleteCustomerProfile.as_view(),
        name='api_customerprofile_detail_update'),
    url(r'^$', ListCreateCustomerProfile.as_view(),
        name='api_customerprofile_list_create')
]