from django.contrib import admin

from tasktracker.models import Status, Task

# Register your models here.

admin.site.register(Status)

admin.site.register(Task)