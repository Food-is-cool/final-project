from django.conf.urls import url, include

urlpatterns = [
url(r'^trucks/', include('trucks.urls')),
url(r'^customers/', include('customers.urls')),
url(r'^groups/', include('mainsite.urls_group')),
url(r'^profiles/', include('mainsite.urls_profile')),
url(r'^users/', include('mainsite.urls_user')),
]
