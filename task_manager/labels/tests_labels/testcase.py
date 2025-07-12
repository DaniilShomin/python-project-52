from django.test import TestCase, Client
from ..models import Labels
from task_manager.users.models import Users


class LabelsTestCase(TestCase):
    fixtures = ['labels.json', 'users.json']

    def setUp(self):
        self.client = Client()
        self.label = Labels.objects.get(pk=1)
        self.user = Users.objects.get(pk=1)

        self.valid_data = {
            'name': 'Test Label',
        }

        self.update_data = {
            'name': 'Updated Label',
        }

        
