from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from tasktracker.models import Task, Status
from tasktracker.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

@login_required
def indextasks (request):
    print(request.user)
    tasks = Task.objects.filter(user = request.user).order_by('due_datetime')
    context = {'tasks': tasks}
    return render (request, "tasktracker/indextasks.html", context)


def login_view(request):
    print(request.user)
    if request.method == 'GET':
        login_form = UserLoginForm()
        context = {'login_form': login_form}
        return render (request, "tasktracker/login_page.html", context)
    else:
        login_form = UserLoginForm(data=request.POST)
        # Валидация
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Аутентификация
            user = auth.authenticate(username=username, password=password)
            if user:
                # авторизация
                auth.login(request, user)
                return HttpResponseRedirect('/tasks')
        
        context = {'login_form': login_form}
        print(login_form.errors)
        return render (request, "tasktracker/login_page.html", context)
    
def register_view(request):
    if request.method == 'POST':
        register_form = UserRegistrationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.save()
            return HttpResponseRedirect('/tasks/login')
        context = {'register_form': register_form}
        return render(request, 'tasktracker/register_page.html', context)
    elif request.method == 'GET':
        register_form = UserRegistrationForm()
        context = {'register_form': register_form}
        return render(request, 'tasktracker/register_page.html', context)
    
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/tasks')

def teams_view(request):
    return render (request, "tasktracker/teams.html")