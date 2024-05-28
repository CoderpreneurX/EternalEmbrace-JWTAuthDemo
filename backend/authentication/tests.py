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
        test_user_creds = {
            'username': 'itz_test_user',
            'password': 'Testuser12345',
        }

        User.objects.create_user(**test_user_creds)

        url = reverse('login-user')
        response = self.client.post(url, test_user_creds)

        self.assertEqual(response.status_code, 200)

        return response.data['access']
    
    def test_register_profile(self):
        access_token = self.test_login_user()

        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'country': 'India',
            'city': 'Batala',
        }
        
        url = reverse('create-user-profile')
        response = self.client.post(url, data, HTTP_AUTHORIZATION=f'Bearer {access_token}')

        print(response.data)