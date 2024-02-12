from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 50, verbose_name='Название новости')
    anons = models.CharField(max_length = 255, verbose_name='Анонс новости')
    full_text = models.TextField('Новость')
    date = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'