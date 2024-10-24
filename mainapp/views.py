from django.shortcuts import render, HttpResponse


def index(request):
    return render (request, "mainapp/main.html")

def about_me(request):
    return render (request, "mainapp/about_me.html")