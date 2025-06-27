from django.shortcuts import redirect, render
from django.views import View

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