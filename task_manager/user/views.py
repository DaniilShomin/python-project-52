from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Users
from .forms import CreateUserForm

# Create your views here.
class IndexView(View):
    def get(self,request):
        users = Users.objects.all()
        return render(
            request,
            'user/index.html',
            context={
                'users': users
            },
        )
    

class CreateUserView(View):
    def get(self,request):
        form = CreateUserForm()
        return render(
            request,
            'user/create.html',
            context={
                'form': form
            },
        )

    def post(self,request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('index')
        return render(
            request,
            'user/create.html',
            context={
                'form': form
            }
        )
    
class UpdateUserView(LoginRequiredMixin, View):
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not logged in! Please sign in.'))
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,pk):
        user_id = request.user.id
        if user_id != int(pk):
            if not request.user.is_superuser:
                messages.error(request, _('You do not have permission to change another user.'))
                return redirect('users')
        user = Users.objects.get(id=pk)
        form = CreateUserForm(instance=user)
        return render(
            request,
            'user/update.html',
            context={
                'form': form,
                'user': user
            }
        )
    
    def post(self,request,pk):
        user = Users.objects.get(id=pk)
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, _("User successfully changed."))
            return redirect('users')
        return render(
            request,
            'user/update.html',
            context={
                'form': form,
                'user': user
            }
        )