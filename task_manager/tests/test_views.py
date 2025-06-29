from django.test import TestCase
from django.urls import reverse
from task_manager.user.forms import CreateUserForm
from datetime import date

class HomePageTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('index'))
    
    def test_home_page(self):
        # status_code
        self.assertEqual(self.response.status_code, 200)

        # template
        self.assertTemplateUsed(self.response, 'index.html')

        # contains correct html
        self.assertContains(self.response, 'Greetings from Hexlet!')

        # does not contain incorrect html
        self.assertNotContains(self.response, "This text shouldn't be here")


class CreateUserViewTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword',
            'confirm_password': 'testpassword',
            'created_at': date.today(),
        }
        self.response = self.client.get(reverse('create_user'))
    
    def test_create_user(self):
        # status_code
        self.assertEqual(self.response.status_code, 200)

        # template
        self.assertTemplateUsed(self.response, 'user/create.html')
        
        # form
        self.assertIsInstance(self.response.context['form'], CreateUserForm)