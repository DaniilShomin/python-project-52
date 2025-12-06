from task_manager.labels.forms import LabelForm
from task_manager.labels.tests.testcase import LabelTestCase


class LabelTestForms(LabelTestCase):
    def test_valid_data(self):
        form = LabelForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_missing_data(self):
        form = LabelForm(data={"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_duplicate_name(self):
        form = LabelForm(data={"name": self.label.name})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
