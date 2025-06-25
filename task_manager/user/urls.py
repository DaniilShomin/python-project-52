from django.urls import path
from task_manager.user.views import (
    IndexView,
    CreateUserView
)

urlpatterns = [
    path('', IndexView.as_view(), name='users'),
    path('create/', CreateUserView.as_view(), name='create_user'),
]