from django.shortcuts import render
from dinomania.models import New, Dino

# Create your views here.

def main(request):
    return  render(request, 'index.html')

def news(request):
    page = 'news'
    news =  New.objects.all()
    return  render(request, 'news.html', {'page':page, 'news': news})
