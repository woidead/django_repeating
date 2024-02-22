# Generated by Django 4.2.3 on 2024-02-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название новости')),
                ('anons', models.CharField(max_length=225, verbose_name='Анонс новости')),
                ('full_text', models.TextField(verbose_name='Новость')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
