from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile

class TestUserAndProfileModels(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        test_user_creds = {
            'username': 'itz_test_user',
            'email': 'testuser@testing.site',
            'password': 'Testuser12345',
        }

        url = reverse('register-user')
        response = self.client.post(url, test_user_creds)

        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        self.test_register_user()
        test_user_creds = {
            'username': 'itz_test_user',
            'password': 'Testuser12345',
        }

        url = reverse('login-user')
        response = self.client.post(url, test_user_creds)

        print(response.data)

        self.assertEqual(response.status_code, 200)