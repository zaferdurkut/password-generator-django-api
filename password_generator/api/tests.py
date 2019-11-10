from django.test import TestCase
from api.models import Password


class PasswordTest(TestCase):
    """ Test module for Password model """

    def setUp(self):
        Password.objects.create(
            password='Test1')
        Password.objects.create(
            password='Test2')

    def test_password(self):
        password_test1 = Password.objects.get(password='Test1')
        password_test2 = Password.objects.get(password='Test2')
        self.assertEqual(
            password_test1.get_password(), "Test1.")
        self.assertEqual(
            password_test2.get_password(), "Test2")
