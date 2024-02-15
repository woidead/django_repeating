from django.urls import path
from news.views import news_home, create

urlpatterns = [
    path('', news_home, name='news_home'),
    path('create', create, name='create_news'),
]
# "http://127.0.0.1:8000/news/create"