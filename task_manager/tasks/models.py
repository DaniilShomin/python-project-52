from django.db import models
from task_manager.statuses.models import Statuses
from task_manager.users.models import Users

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(unique=True)
    description = models.TextField(null=True , blank=True)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, related_name='status', null=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='author', null=True)
    executor = models.ForeignKey(Users, on_delete=models.CASCADE , related_name='executor', null=True)
    label = models.CharField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)