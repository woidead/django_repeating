from django.urls import path
from users.views import (UserLoginView, logout_view, profile_view, CreateUserView)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path("profile/", profile_view, name="profile"),
    path('registration/', CreateUserView.as_view(), name='registration'),  # регистрация
]