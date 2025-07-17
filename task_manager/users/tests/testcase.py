from django.test import Client, TestCase

from task_manager.tasks.models import Task

from task_manager.users.models import User


class UserTestCase(TestCase):
    fixtures = ["test_users.json", "test_tasks.json", "test_statuses.json"]

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.task = Task.objects.get(pk=1)

        self.valid_data = {
            "first_name": "Tom",
            "last_name": "Brady",
            "username": "TomBrady",
            "password": "Tom123",
            "confirm_password": "Tom123",
        }
