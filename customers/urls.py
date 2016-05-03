from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include

from customers.views import DetailUpdateDeleteCustomerProfile, DetailCurrentCustomer, \
    ListCreateCustomerProfile

urlpatterns = [
    url(r'^current/$', DetailCurrentCustomer.as_view(),
        name='api_current_customer'),
    url(r'^(?P<pk>\d+)$',
        DetailUpdateDeleteCustomerProfile.as_view(),
        name='api_customerprofile_detail_update'),
    url(r'^$', ListCreateCustomerProfile.as_view(),
        name='api_customerprofile_list_create')
]