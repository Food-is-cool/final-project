from django.conf.urls import url
from mainsite.views import ListGroups

urlpatterns = [
url(r'^$', ListGroups.as_view(),
    name='api_list_groups')
]