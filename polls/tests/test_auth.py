from django.contrib.auth.models import User
from django.test import TestCase
from django.shortcuts import reverse


class BasicAuthTests(TestCase):
    """Basic authentication"""

    def setUp(self):
        self.user = {
            'username': 'wave49192',
            'password': 'wavegamer123'
        }
        User.objects.create_user(**self.user)

    def test_login(self):
        response = self.client.post(reverse('login'), self.user)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('polls:index'))
        self.assertTrue(response.context['user'].is_authenticated)

    def test_logout(self):
        self.client.post(reverse('login'), self.user)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('polls:index'))
        self.assertFalse(response.context['user'].is_authenticated)
