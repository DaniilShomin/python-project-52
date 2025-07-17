from django.test import Client, TestCase

from task_manager.users.models import User

from task_manager.statuses.models import Status


class StatusTestCase(TestCase):
    fixtures = ["test_statuses.json", "test_users.json"]

    def setUp(self):
        self.client = Client()
        self.status = Status.objects.get(pk=1)
        self.user = User.objects.get(pk=1)

        self.valid_data = {"name": "Test Status"}

        self.update_data = {"name": "Updated Status"}
