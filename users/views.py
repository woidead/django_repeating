from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from users.forms import UserLoginForm
from django.contrib.auth import logout
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

def logout_view(request):
    logout(request)
    return redirect('home')