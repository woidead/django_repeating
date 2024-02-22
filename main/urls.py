from django.urls import path
from main.views import index, contact
urlpatterns = [
    path('', index, name='home'),
    path("contact", contact, name="contact"),
]