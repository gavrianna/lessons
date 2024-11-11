from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from tasktracker.models import Task


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']

class TasksCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_datetime']

class TasksEditForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_datetime', 'status']