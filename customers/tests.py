from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from customers.models import CustomerProfile
from trucks.models import TruckProfile
from rest_framework.test import APIClient


class CustomerTests(TestCase):

    def test_create_truck(self):
        url = reverse('api_createcustomer_user')
        data = {'username':'test_customer', 'password':'password!'}
        response = self.client.post(url,data)
        # assert response

        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.groups.first().name, 'customers')
        self.assertEqual(CustomerProfile.objects.count(), 1)

    def test_like_truck(self):
        customeruser = User.objects.create_user(username='customeruser', password='password')
        customer_profile = CustomerProfile.objects.create(user=customeruser)
        truckuser= User.objects.create_user('truckuser', 'password')
        client = APIClient()
        client.login(username='customeruser', password='password')
        truck_profile = TruckProfile.objects.create(user=truckuser)

        url = reverse('api_liketruck')
        data = {'truck_id':truck_profile.id, 'liked':True}
        response = client.patch(url, data, format='json')
        print(response.data)
        self.assertEqual(customer_profile.liked_trucks.count(), 1)


    # def test_unlike_truck(self):
    #     customeruser = User.objects.create_user(username='customeruser',
    #                                             password='password')
    #     customer_profile = CustomerProfile.objects.create(user=customeruser)
    #     truckuser = User.objects.create_user('truckuser', 'password')
    #     client = APIClient()
    #     client.login(username='customeruser', password='password')
    #     truck_profile = TruckProfile.objects.create(user=truckuser)
    #
    #     url = reverse('api_liketruck')
    #     data = {'truck_id': truck_profile.id, 'liked': True}
    #     response = client.patch(url, data, format='json')
    #     print(response.data)
    #     self.assertEqual(customer_profile.liked_trucks.count(), 1)


