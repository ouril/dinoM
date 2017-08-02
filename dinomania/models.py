from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
# Create your models here.


class AntiTrashMixin(object):
    def save(self, *args, **kwargs):
        try:
            this_record = New.objects.get(id = self.id)
            if this_record.img != self.img:
                this_record.img.delete(save=False)
        except:
            pass
        super(New, self).save(*args, **kwargs)

class New(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name='Загаловок новости')

    where_from = models.URLField(verbose_name='Источник',  blank=True)
    dino = models.ForeignKey('Dino', null=True)
    time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время', null=True)
    body = models.TextField(verbose_name='Синапсис новости', blank=True)
    img = models.ImageField(upload_to='test', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    content2 = RichTextUploadingField(blank=True, null=True)
    def __str__(self):
        return self.name


class Dino(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название динозавра')
    info = models.URLField(verbose_name='Статья', blank=True)
    about = models.TextField(blank=True)
    foto = models.ImageField(upload_to='test', blank=True)

    suborder = models.ForeignKey('SubOrder', null=True)

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

    def __str__(self):
        return self.name

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

class SubOrder(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Название отряда')
    site = models.URLField(verbose_name='Статья', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    order = models.ForeignKey('Order', null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(
        max_length=36, unique=True, verbose_name='Название отряда')
    site = models.URLField(verbose_name='Статья', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):

    author_id = models.ForeignKey(User)
    about = models.ForeignKey('New')
    content = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='дата и время', null=True)

