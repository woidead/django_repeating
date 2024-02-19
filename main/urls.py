from django.urls import path
from main.views import index, contact, profile_view

urlpatterns = [
    path('', index, name='home'),
    path("contact", contact, name="contact"),
    path("profile", profile_view, name="profile"),
]