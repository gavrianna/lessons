from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from tasktracker.models import Task, Status
from tasktracker.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from tasktracker.forms import TasksCreationForm
from tasktracker.forms import TasksEditForm 

@login_required
def indextasks (request):
    if request.method == 'GET':
        print(request.user)
        tasks = Task.objects.filter(user = request.user).order_by('due_datetime')
        creation_form = TasksCreationForm ()
        edit_form = TasksEditForm ()
        context = {'tasks': tasks, 'creation_form': creation_form, "edit_form": edit_form}
        return render (request, "tasktracker/indextasks.html", context)
    else:
        creation_form = TasksCreationForm(data=request.POST)
        if creation_form.is_valid():
            task = creation_form.save(commit=False)
            task.user = request.user
            task.status_id = 1
            task.save()
        return HttpResponseRedirect('/tasks')


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

def get_task_info(request, task_id):
    
    task = Task.objects.get(id = task_id)
    task_json = {
        "task_id": task.id,
        "title": task.title,
        "description": task.description,
        "due_datetime": task.due_datetime.strftime('%Y-%m-%d %H:%M'),
        "status_id": task.status.id
    }
    # нужно отдать json

    return JsonResponse(task_json)

def edit_task_view(request):
    task_id = request.POST.get('edit_task_id')
    task = Task.objects.get(id=task_id, user=request.user)
    form_edit = TasksEditForm(request.POST, instance=task)
    if form_edit.is_valid():
        form_edit.save()
        return HttpResponseRedirect('/tasks')