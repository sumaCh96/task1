from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse



class ProductTestcase(APITestCase):

    def test_prod(self):
        response = self.client.get(reverse('product'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)