from django.shortcuts import render
from dinomania.models import New, Dino, Book, SubOrder
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class MainView(ListView):
    template_name = "index.html"
    model = New
    paginate_by = 3
    queryset = New.objects.order_by("time").reverse()[:3]


class NewsView(ListView):
    template_name = "news.html"
    paginate_by = 3
    model = New
    queryset = New.objects.all().order_by("time").reverse()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        return context
        print(context)

def sort_for_time(request):

    context = New.objects.all().order_by("time").reverse(
    ) if request.GET.get('reversed') else New.objects.all().order_by("time")

    paginator = Paginator(context, 3)
    page = request.GET.get('page')
    try:
        num_page = paginator.page(page)
    except PageNotAnInteger:
        num_page = paginator.page(1)
    except PageNotAnInteger:
        num_page = paginator.page(paginator.num_pages)
    return render(request, 'news.html', {"object_list": num_page})


class BooksView(ListView):
    model = Book
    template_name = "books.html"
    paginate_by = 12

class DinoView(ListView):
    model = Dino
    template_name = "dino.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sub"] = SubOrder.objects.all()
        return context
        print(context)




class NewsDetail(DetailView):
    model = New
    template_name = "news_detail.html"

class BooksDetail(DetailView):
    model = Book
    template_name = "books_detail.html"

class DinoDetail(DetailView):
    model = Dino
    template_name = "dino_detail.html"