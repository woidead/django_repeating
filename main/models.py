from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='media')