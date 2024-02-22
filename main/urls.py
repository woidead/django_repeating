from django.urls import path
from main.views import index, contact, logout_view

urlpatterns = [
    path('', index, name='home'),
    path("contact", contact, name="contact"),
]