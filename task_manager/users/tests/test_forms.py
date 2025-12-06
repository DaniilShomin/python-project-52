from task_manager.users.forms import UserForm
from task_manager.users.tests.testcase import UserTestCase


class UserTestForms(UserTestCase):
    def test_valid_data(self):
        form = UserForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_missing_data(self):
        # Missing full data
        form = UserForm(data={})
        self.assertFalse(form.is_valid())

        # Missing first_name and last_name
        data = self.valid_data.copy()
        data["first_name"] = ""
        data["last_name"] = ""
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())

        # Missing username
        data = self.valid_data.copy()
        data["username"] = ""
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_unique_username_validation(self):
        data = self.valid_data.copy()
        data["username"] = self.user1.username
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_username_too_long(self):
        long_username = "a" * 151
        data = self.valid_data.copy()
        data["username"] = long_username
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_password_mismatch(self):
        data = self.valid_data.copy()
        data["password2"] = "wrongpass"
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())

    def test_short_password(self):
        data = self.valid_data.copy()
        data["password1"] = "ab"
        data["password2"] = "ab"
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())
