from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from task_manager.forms import LoginForm
from task_manager.user.models import Users


class IndexView(View):
    def get(self, request):
        return render(
            request,
            'index.html',
            context={}
        )
    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(
            request,
            'login.html',
            context={
                'form': form,
            }
        )
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, _('Вы залогинены'))
                return redirect('index')
            else:
                form.add_error(None, _(
                    "Please enter a correct username and password. "
                    "Note that both fields may be case-sensitive."
                ))
        return render(
            request, 
            'login.html', 
            context = {
                'form': form
                }
            )
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, _('Вы разлогинены'))
        return redirect('index')