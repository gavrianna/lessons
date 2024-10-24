from django.urls import path, include
from tasktracker.views import indextasks, login_view, register_view, teams_view, logout_view
app_name = "tasktrack"
urlpatterns = [
    path('', indextasks), # main page 
    path('login/', login_view),
    path('register', register_view),
    path('teams', teams_view),
    path('logout', logout_view),
]
