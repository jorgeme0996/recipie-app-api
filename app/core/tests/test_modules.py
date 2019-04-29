from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = '123456789'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def new_user_email_normalized(self):
        """Test the email foa a new user is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())