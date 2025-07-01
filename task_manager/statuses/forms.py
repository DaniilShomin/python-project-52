from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Statuses


class CreateStatusesForm(forms.ModelForm):

    class Meta:
        model = Statuses
        fields = [
            'name',
        ]

    def clean_name(self):
        if Statuses.objects.filter(name=self.cleaned_data['name']).exists():
            raise forms.ValidationError(
                _('Task status with this Name already exists.')
            )
        return self.cleaned_data['name']