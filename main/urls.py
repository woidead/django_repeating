from django.urls import path
from main.views import index, contact, profile_view, logout_view

urlpatterns = [
    path('', index, name='home'),
    path("contact", contact, name="contact"),
    path("profile", profile_view, name="profile"),
    path('logout/', logout_view, name='logout_acc')
]