from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 50, verbose_name='Название новости')
    anons = models.CharField('Анонс новости', max_length = 225)
    full_text = models.TextField('Новость')
    date = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"


    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'