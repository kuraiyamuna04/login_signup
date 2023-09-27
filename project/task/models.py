from django.db import models

from app.models import CustomUser


class TaskModel(models.Model):
    task = models.CharField(max_length=500)
    due_date = models.DateField()
    assigned_by = models.CharField(max_length=20, default=None)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.task
