from django.conf.urls import url
from mainsite.views import DetailCurrentUser, DetailUser

urlpatterns = [
    url(r'^(?P<pk>\d+)$', DetailUser.as_view(),
        name='api_detail_user'),
    url(r'^current/$', DetailCurrentUser.as_view(),
        name='api_current_user'),
]
