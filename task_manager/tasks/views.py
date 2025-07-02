from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

# from .forms import CreateUserForm
from .forms import SearchTaskForm
from .models import Tasks


class IndexTaskView(View):
    def get(self, request):
        if request.GET:
            form = SearchTaskForm(data=request.GET)
        else:  
            form = SearchTaskForm(
                initial={
                    'status': '',
                    'executor': '',
                    'label': ''
                }
            )
        tasks = Tasks.objects.all()
        return render(
            request, 
            'tasks/index.html', 
            context={
                'form': form,
                'tasks': tasks
            }
        )
    
class CreateTaskView(LoginRequiredMixin, View):
    pass

class DeleteTaskView(LoginRequiredMixin, View):
    pass

class UpdateTaskView(LoginRequiredMixin, View):
    pass