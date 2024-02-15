from django.shortcuts import render, redirect
from news.models import Article
from news.forms import ArticleForm
from django.views.generic import DetailView, UpdateView
# Create your views here.

def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/index.html', {'news':news})

class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewsUpdatelView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm


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