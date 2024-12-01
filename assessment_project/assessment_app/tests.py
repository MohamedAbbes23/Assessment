from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):

    def setUp(self):
        
        self.client = APIClient()
        self.register_url = '/api/register/'  
        self.login_url = '/api/token/'  
        self.user_data = {
            "username": "testuser",
            "password": "testpassword123",
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_register_user(self):
        
        data = {
            "username": "newuser",
            "password": "newpassword123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("username", response.data)
        self.assertEqual(response.data["username"], "newuser")

    def test_login_user(self):
        
        data = {
            "username": "testuser",
            "password": "testpassword123",
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_invalid_login(self):
        
        data = {
            "username": "testuser",
            "password": "wrongpassword",
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)



