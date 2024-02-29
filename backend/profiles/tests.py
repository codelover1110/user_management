# profiles/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserProfile

class UserProfileModelTest(TestCase):
    def setUp(self):
        # Create a sample user profile for testing
        self.user = UserProfile.objects.create(
            first_name='John',
            surname='Doe',
            email='john.doe@example.com',
            phone_number='+447912345678'
        )

    def test_user_profile_creation(self):
        # Test that a user profile can be created and saved
        self.assertEqual(UserProfile.objects.count(), 1)
        saved_user = UserProfile.objects.get(id=1)
        self.assertEqual(saved_user.first_name, 'John')

class UserProfileAPITest(TestCase):
    def setUp(self):
        # Set up an API client and sample user data for testing
        self.client = APIClient()
        self.user_data = {
            'first_name': 'John',
            'surname': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '+447912345678'
        }

    def test_create_user_profile(self):
        # Test creating a new user profile via the API
        url = reverse('userprofile-list')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user_profile_list(self):
        # Test retrieving a list of user profiles via the API
        url = reverse('userprofile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # No profiles initially

    def test_get_user_profile_detail(self):
        # Test retrieving details of a user profile via the API
        user = UserProfile.objects.create(**self.user_data)
        url = reverse('userprofile-detail', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')
