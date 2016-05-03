from django.conf.urls import url
from mainsite.views import ListCreateProfile, DetailProfile

urlpatterns = [
    url(r'^$', ListCreateProfile.as_view(),
        name='api_list_groups'),
    url(r'^(?P<pk>\d+)$', DetailProfile.as_view(),
        name='api_detail_user'),
]