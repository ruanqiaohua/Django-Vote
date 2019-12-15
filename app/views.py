from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def index(request):
    return render(request, template_name='app/index.html')

def login(request):
    return HttpResponse("login")

def register(request):
    return HttpResponse("register")