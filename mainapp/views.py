from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('Это главная!')

def about_me(request):
    return HttpResponse('Это про меня')