from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.user.models import Users

class CreateUserForm(forms.ModelForm):
    password = forms.CharField(
        label=_("Password"), 
        widget=forms.PasswordInput,
    )
    confirm_password = forms.CharField(
        label=_("Confirm Password"), 
        widget=forms.PasswordInput,
    )

    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'confirm_password'
        ]
        help_texts = {
            'username': _("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
            'password': _("<ul><li>Your password must be at least 3 characters long.</ul></li>"),
            'confirm_password': _('To confirm, please enter your password again.'),
        }
