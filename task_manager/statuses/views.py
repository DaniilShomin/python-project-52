from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from .forms import CreateStatusesForm
from .models import Statuses


# Create your views here.
class IndexStatusesView(LoginRequiredMixin, View):
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not logged in! Please sign in.'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        statuses = Statuses.objects.all().order_by('id')
        return render(
            request,
            'statuses/index.html',
            context={
                'statuses': statuses,
            }
        )


class CreateStatusesView(LoginRequiredMixin, View):
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not logged in! Please sign in.'))
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form = CreateStatusesForm()
        return render(
            request,
            'statuses/create.html',
            context={
                'form': form,
            }
        )

    def post(self, request):
        form = CreateStatusesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Status successfully created'))
            return redirect('statuses')
        return render(
            request,
            'statuses/create.html',
            context={
                'form': form,
            }
        )
        

class UpdateStatusesView(LoginRequiredMixin, View):
    pass


class DeleteStatusesView(LoginRequiredMixin, View):
    pass