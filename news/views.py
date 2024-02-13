from django.shortcuts import render
from news.models import Article

# Create your views here.

def news_home(request):
    news = Article.objects.order_by('-date')[:2]
    return render(request, 'news/index.html', {'news':news})