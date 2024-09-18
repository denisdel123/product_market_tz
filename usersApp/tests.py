from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):

    def test_user_registration(self):
        data = {
            "email": "test@mail.ru",
            "password1": "Q23wer344",
            "password2": "Q23wer344"
        }

        url = reverse('usersApp:user-create')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_registration_invalid_data(self):
        data = {
            "email": "test-32",
            "password1": "55555",
            "password2": "55555"
        }

        url = reverse('usersApp:user-create')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
