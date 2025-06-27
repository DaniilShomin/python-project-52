from django.contrib.auth import authenticate
from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.user.models import Users


class LoginForm(forms.Form):
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        required=True,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(),
        required=True
    )
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
        
    #     error_message = _(
    #         "Please enter a valid username and password. "
    #         "Both fields may be case sensitive."
    #     )

    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #         if user is None:
    #             raise forms.ValidationError(error_message)
        
    #     return cleaned_data

