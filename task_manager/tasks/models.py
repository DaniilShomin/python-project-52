from django.db import models
from task_manager.statuses.models import Statuses
from task_manager.users.models import Users

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(unique=True)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, related_name='status', null=True, blank=True)
    autor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='autor')
    executor = models.ForeignKey(Users, on_delete=models.CASCADE , related_name='executor', null=True, blank=True)
    label = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)