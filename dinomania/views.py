from django.shortcuts import render
from dinomania.models import New, Dino, Book
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
#def mainview(request):
#    news = New.objects.all()
#    return render(request, "index.html", {'news': news})

class MainView(ListView):
    template_name = "index.html"
    model = New
    paginate_by = 3    
#def newsview(request):
 #   news = New.objects.all()
  #  return render(request, "news.html", {'news': news})

class NewsView(MainView):
    template_name = "news.html"
    paginate_by = 12

class BooksView(MainView):
    model = Book
    template_name = "books.html"
    paginate_by = 12

class NewsDetail(DetailView):
    model = New
    template_name = "news_detail.html"
        