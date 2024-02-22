from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

class CreateUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Youve successfully signed up!'

    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data()
        context['title'] = 'Доставка еды | Регистрация'
        return context