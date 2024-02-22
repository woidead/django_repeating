from django.urls import path
from django.contrib.auth.decorators import login_required
from users.views import (UserLoginView, logout_view, profile_view, 
                         CreateUserView, UserProfileView)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path("profile/", profile_view, name="profile"),
    path('registration/', CreateUserView.as_view(), name='registration'),  #регистрация
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name='edit_profile'),  #Редактировать профиль
]