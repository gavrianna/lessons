from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from tasktracker.models import Task
from django import forms


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']

class TasksCreationForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2 fs-4', 'placeholder':'Заголовок задачи'}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_datetime']

class TasksEditForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'edit_task_description form-control'}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_datetime', 'status']