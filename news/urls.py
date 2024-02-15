from django.urls import path
from news.views import news_home, create, NewsDetailView

urlpatterns = [
    path('', news_home, name='news_home'),
    path('create', create, name='create_news'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail')
]
# "http://127.0.0.1:8000/news/"
