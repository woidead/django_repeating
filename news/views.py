from django.shortcuts import render, redirect
from news.models import Article
from news.forms import ArticleForm
# Create your views here.

def news_home(request):
    news = Article.objects.order_by('-date')[:2]
    return render(request, 'news/index.html', {'news':news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_home")
        else:
            error = "Форма неверная"

    form = ArticleForm()
    context = {
        'form': form,
        'error':error
        }
    return render(request, 'news/create.html', context)