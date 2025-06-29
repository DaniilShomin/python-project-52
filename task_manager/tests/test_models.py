from django.test import TestCase
from task_manager.user.models import Users
from datetime import date


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = Users.objects.create_user(
            username="test_user",
            password="test_password",
            first_name="Test",
            last_name="User",
            created_at=date.today(),
        )
    
    def test_user_model(self):
        user = Users.objects.get(id=self.user.id)
        self.assertEqual(user.username, 'test_user')
        self.assertTrue(user.check_password('test_password'))
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')

    def test_username_uniqueness(self):
        with self.assertRaises(Exception):
            Users.objects.create_user(
                username='test_user',  # Username already exists
                password='testpass123',
                first_name="Test",
                last_name="User",
                created_at=date.today(), 
            )