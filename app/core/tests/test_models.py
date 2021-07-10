from django.test import TestCase
from django.contrib.auth import get_user_model
#getuser helper function from django

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email="sai@gmail.com"
        password="sai"
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email="sai@GMAIL.COM"
        user= get_user_model().objects.create_user(email,'sai')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'sai')
        #here with is used instead of try chatch 
    
    def test_create_new_superuser(self):
        """test creating a new super user"""
        user= get_user_model().objects.create_superuser(
            'sai@gmail.com',
            'sai'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    

