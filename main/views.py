from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def index(request):
    context = {
        'title' :' Главная страница!!',
        'value' : ['aziz', 'oomat', 'raziya'],
        'num': 10,
        'dict': {
            'age':14,
            "car":'bmw',
            "hobby":"football"
        }
        }
    return render(request, 'main/index.html', context)

def contact(request):
    return render(request, 'main/contact.html')

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')


def logout_view(request):
    logout(request)
    return redirect('profile')