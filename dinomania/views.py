from django.shortcuts import render
from dinomania.models import New, Dino, Book
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class MainView(ListView):
    template_name = "index.html"
    model = New
    paginate_by = 3    

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['object_list'] = New.objects.order_by("time").reverse()[:3]
        return context

class NewsView(ListView):
    template_name = "news.html"
    paginate_by = 12
    model = New

class BooksView(NewsView):
    model = Book
    template_name = "books.html"
    

class NewsDetail(DetailView):
    model = New
    template_name = "news_detail.html"
        