from django.urls import path
from news.views import news_home

urlpatterns = [
    path('', news_home, name='news_home'),
]