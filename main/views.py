from django.shortcuts import render
from django.http import HttpResponse
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

def profile_view(request):
    return render(request, 'main/profile.html')