from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from .forms import CreateLabelsForm
from .models import Labels


class BaseLabelsView(LoginRequiredMixin, View):
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not logged in! Please sign in.'))
        return super().dispatch(request, *args, **kwargs)
    
class IndexLabelsView(BaseLabelsView):
    def get(self, request):
        labels = Labels.objects.all()
        return render(
            request, 
            'labels/index.html', 
            context={
                'labels': labels
            }
        )
    

class CreateLabelsView(BaseLabelsView):
    def get(self, request):
        return self._render_form(request, CreateLabelsForm())

    def post(self, request):
        form = CreateLabelsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('labels')
        return self._render_form(request, form)

    def _render_form(self, request, form):
        return render(
            request, 
            'labels/create.html', 
            context={
                'form': form
            }
        )


class UpdateLabelsView(BaseLabelsView):
    pass


class DeleteLabelsView(BaseLabelsView):
    pass