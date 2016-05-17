from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from unittest.mock import patch

# Create your tests here.
from customers.models import CustomerProfile
from notifications.models import SMSNotifications


class TwilioTests(TestCase):

    @patch('notifications.views.TwilioRestClient')
    def test_SMS_notifications(self, client):
        customeruser = User.objects.create_user(username='customeruser',
                                                password='password')
        customer_profile = CustomerProfile.objects.create(user=customeruser,
                                                          want_texts=True,
                                                          mobile_number='12345678910')
        notification = SMSNotifications.objects.create(text_content = "this is a test")
        url = reverse('trigger_text_send', kwargs={'notification_id':notification.id})
        self.client.get(url)
        self.assertTrue(client.return_value.messages.create.called)


        #TODO: Make model names singular

