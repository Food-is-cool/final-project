from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
from trucks.models import TruckProfile


class TruckTests(TestCase):

    def test_create_truck(self):
        url = reverse('api_listcreate_truckuser')
        data = {'username':'test_truck', 'password':'password!'}
        response = self.client.post(url,data)
        # assert response
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.groups.first().name, 'trucks')
        self.assertEqual(TruckProfile.objects.count(), 1)

