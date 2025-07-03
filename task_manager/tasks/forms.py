'''
class Tasks(models.Model):
    name = models.CharField(unique=True)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, related_name='status')
    autor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='autor')
    executor = models.ForeignKey(Users, on_delete=models.CASCADE , related_name='executor')
    label = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)'''

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Tasks


class SearchTaskForm(forms.ModelForm):
    self_tasks = forms.BooleanField(
        label=_('Only my tasks'),
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    class Meta:
        model = Tasks
        fields = [
            'status',
            'executor',
            'label',
            'self_tasks',
        ]
        labels = {
            'status': _('Status'),
            'executor': _('Executor'),
            'label': _('Label'),
        }
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'executor': forms.Select(attrs={'class': 'form-control'}),
            'label': forms.Select(attrs={'class': 'form-control'}),
        }
        empty_label = {
            'status': '---------',
            'executor': '---------',
            'label': '---------',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].required = False
        self.fields['executor'].required = False
        self.fields['label'].required = False


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'label',
        ]
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'label': _('Labels'),
        }
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'label': forms.Select(attrs={'class': 'form-control', 'multiple': True}),
        }
        empty_label = {
            'status': '---------',
            'executor': '---------',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['executor'].required = False
        self.fields['label'].required = False
