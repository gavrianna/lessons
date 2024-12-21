from django.urls import path, include
from tasktracker.views import indextasks, login_view, register_view, teams_view, logout_view, get_task_info, edit_task_view
app_name = "tasktrack"
urlpatterns = [
    path('', indextasks), # main page 
    path('login/', login_view),
    path('register', register_view),
    path('teams', teams_view),
    path('logout', logout_view),
    path('get_task_info/<int:task_id>', get_task_info), # /tasks/get_task_info/1 
    path('edit_task_view', edit_task_view)
]
