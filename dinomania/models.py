from django.db import models

# Create your models here.


class New(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Загаловок новости')
    slug_name = models.CharField(max_length=120, unique=True, verbose_name='Синапсис новости', blank=True, null=True)
    where_from = models.URLField(verbose_name='Источник',  blank=True)
    dino = models.ForeignKey('Dino', null=True)
    cat = models.ForeignKey('Category', null=True)
    time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время', null=True)
    body = models.TextField(blank=True)
    img = models.ImageField(upload_to='test', blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Загаловок новости')
    body = models.TextField(blank=True)

    def __str__(self):
        return self.name
 
class Dino(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название динозавра')
    info = models.URLField(verbose_name='Статья', blank=True)
    about = models.TextField(blank=True)
    foto = models.ImageField(upload_to='test', blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название книги')
    slug_name = models.CharField(max_length=120, unique=True, verbose_name='Коротко о книге', blank=True, null=True)
    info = models.CharField(max_length=120, unique=True, verbose_name='Издательство - год, и прочее', blank=True, null=True)
    autor = models.ForeignKey('Autor', null=True)
    dino = models.ForeignKey('Dino', null=True)
    site = models.URLField(verbose_name='Статья', blank=True)
    about = models.TextField(blank=True)
    foto = models.ImageField(upload_to='test', blank=True)


class Autor(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя автора')
    site = models.URLField(verbose_name='Статья', blank=True)
    about = models.TextField(blank=True)   

    def __str__(self):
        return self.name

class Resurs(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название сайта')
    site = models.URLField(verbose_name='Статья', blank=True)
    about = models.TextField(blank=True)   

    def __str__(self):
        return self.name