from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'crumble/home.html', {})

def registration(request):
    return render(request, 'crumble/registration.html', {})
