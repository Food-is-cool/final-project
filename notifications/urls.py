from django.conf.urls import url
from twilio.rest.resources import notifications
from notifications import views

urlpatterns = [
    # url(r'^emaillookup/', views.email_list),
    # url(r'^textlookup/', views.text_list),
    url(r'^sendemails/(?P<blast_id>\d+)$',
        views.trigger_email_send, name='trigger_email_send'),
    url(r'^sendtexts/(?P<notification_id>\d+)$',
        views.trigger_text_send, name='trigger_text_send')
]

