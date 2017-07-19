from django.shortcuts import render
from dinomania.models import New, Dino, Book
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class MainView(ListView):
    template_name = "index.html"
    model = New
    paginate_by = 3
    queryset = New.objects.order_by("time").reverse()[:3]


class NewsView(ListView):
    template_name = "news.html"
    paginate_by = 12
    model = New
    queryset = New.objects.all().order_by("time").reverse()

def sort_for_time(request):
    context = New.objects.all().order_by("time").reverse() if request.GET.get('reversed') else New.objects.all().order_by(
        "time")
    return render(request, 'news.html', {"object_list": context})


class BooksView(ListView):
    model = Book
    template_name = "books.html"
    paginate_by = 12

class DinoView(ListView):
    model = Dino
    template_name = "dino.html"
    paginate_by = 20

class NewsDetail(DetailView):
    model = New
    template_name = "news_detail.html"

class BooksDetail(DetailView):
    model = Book
    template_name = "books_detail.html"

class DinoDetail(DetailView):
    model = Dino
    template_name = "dino_detail.html"