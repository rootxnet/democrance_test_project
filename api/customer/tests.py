
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer

class CustomerAPITestCase(APITestCase):

    def setUp(self):
        # Set up any initial data here
        self.customer1 = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            dob="1992-06-25"  # Format needs to be in YYYY-MM-DD for the model
        )
        self.customer2 = Customer.objects.create(
            first_name="Alice",
            last_name="Doe",
            dob="1990-01-30"
        )

    def test_create_customer(self):
        url_reversed = reverse('customer:create')
        url = "/api/v1/create_customer/"
        self.assertEqual(url, url_reversed)
        data = {
            "first_name": "Ben",
            "last_name": "Stokes",
            "dob": "25-06-1991"  # DD-MM-YYYY format for serializer
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 3)
        # also test proper ordering
        self.assertEqual(Customer.objects.last().first_name, 'Ben'
                                                             '')

    def test_create_customer_invalid_date(self):
        url = reverse('customer:create')
        data = {
            "first_name": "Bob",
            "last_name": "Dylan",
            "dob": "31-31-1801"  # Invalid date format
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)