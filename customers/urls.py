from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include

from customers import views
from customers.views import DetailUpdateDeleteCustomerProfile, \
    ListCreateCustomerProfile, CreateCustomerUser, \
    DetailCurrentCustomer, UpdateLikedTrucks

urlpatterns = [
    url(r'^users/$', CreateCustomerUser.as_view(),
       name='api_createcustomer_user'),
    url(r'^users/current/$', DetailCurrentCustomer.as_view(),
        name='api_current_customer'),
    url(r'^users/(?P<pk>\d+)$',
        DetailUpdateDeleteCustomerProfile.as_view(),
        name='api_customerprofile_detail_update'),
    url(r'^users/liketruck/$', UpdateLikedTrucks.as_view(),
        name='api_liketruck'),
    url(r'^$', ListCreateCustomerProfile.as_view(),
        name='api_customerprofile_list_create')
]


# url(r'^users/liketruck/$', UpdateLikedTrucks.as_view()),