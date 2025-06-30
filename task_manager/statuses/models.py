from django.db import models

# Create your models here.
class Statuses(models.Model):
    name = models.CharField()
    create_at = models.DateTimeField(auto_now_add=True)