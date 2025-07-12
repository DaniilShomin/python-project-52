from ..forms import CreateLabelsForm
from .testcase import LabelsTestCase


class LabelsTestForms(LabelsTestCase):
    def test_valid_data(self):
        form = CreateLabelsForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_missing_data(self):
        form = CreateLabelsForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_duplicate_name(self):
        form = CreateLabelsForm(data={'name': self.label.name})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

