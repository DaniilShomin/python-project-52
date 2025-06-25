from django.shortcuts import render
from django.views import View

from task_manager.user.models import (Users)

# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,'user/index.html')
    

class CreateUserView(View):
    def get(self,request):
        users = Users.objects.all()
        return render(
            request,
            'user/create_user.html',
            context={
                'users': users
            },
        )

    def post(self,request):
        ...