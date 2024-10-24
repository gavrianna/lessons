from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}. {self.name}'

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_datetime = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now()+datetime.timedelta(hours=1))
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {self.title} | {self.user}'


