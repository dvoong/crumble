import crumble.forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'crumble/home.html', {})

def registration(request):
    if request.method == 'GET':
        form = crumble.forms.RegistrationForm()
        return render(request, 'crumble/registration.html', {'registration_form': form})
    else:
        form = crumble.forms.RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(user.homepage)
        return render(request, 'crumble/registration.html', {'registration_form': form})
