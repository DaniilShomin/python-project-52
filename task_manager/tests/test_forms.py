from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.forms import LoginForm
from task_manager.users.forms import CreateUserForm

User = get_user_model()


class CreateUserFormTest(TestCase):
    def test_unique_username_validation(self):
        User.objects.create(username="existing_user")
        form_data = {
            "username": "existing_user",
            "first_name": "John",
            "last_name": "Doe",
            "password": "123456",
            "confirm_password": "123456"
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_update_existing_user(self):
        user = User.objects.create(username="existing_user")
        form_data = {
            "username": "existing_user",
            "first_name": "Jane",
            "last_name": "Doe",
            "password": "newpass123",
            "confirm_password": "newpass123"
        }
        form = CreateUserForm(data=form_data, instance=user)
        self.assertTrue(form.is_valid())

    def test_invalid_characters_in_username(self):
        form_data = {
            "username": "user@name#",
            "first_name": "John",
            "last_name": "Doe",
            "password": "123456",
            "confirm_password": "123456"
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)


class LoginFormTest(TestCase):
    def test_valid_login(self):
        User.objects.create_user(username="testuser", password="testpassword")
        form_data = {
            "username": "testuser",
            "password": "testpassword"
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_empty_data(self):
        form_data = {}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)