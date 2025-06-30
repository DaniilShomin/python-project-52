from django.urls import path
from .views import (
    IndexStatusesView,
    CreateStatusesView,
)

urlpatterns = [
    path('', IndexStatusesView.as_view(), name='statuses'),
    path('create/', CreateStatusesView.as_view(), name='create_status'),
]