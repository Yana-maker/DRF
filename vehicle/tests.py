from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Car, Moto



class MaterialsTestCase(APITestCase):

    def setUp(self) -> None:

        self.moto = Moto.objects.create(
            title='test',
            description='test'
        )


    def test_get_list(self):
        """проверка списка сущностей"""

        response = self.client.get(
            ('/moto/list/')
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
