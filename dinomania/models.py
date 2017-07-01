from django.db import models

# Create your models here.


class Dino(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название динозавра')
    info = models.URLField(verbose_name='Статья', blank=True)

    def __str__(self):
        return self.name

class New(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название новости')
    where_from = models.URLField(verbose_name='Источник',  blank=True)
    dino = models.ForeignKey(Dino, null=True)
    time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время', null=True)
    body = models.TextField(blank=True)
    img = models.ImageField(upload_to='test', blank=True)

    def __str__(self):
        return self.name
