from news.models import Article
from django.forms import ModelForm, TextInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text']
        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Анонс статьи'
            }),
            'full_text': Textarea(attrs={
                'class':'form-control',
                'placeholder':'Полная статья'
            }),
        }