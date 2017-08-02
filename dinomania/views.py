from django.shortcuts import render
from dinomania.models import New, Dino, Book, SubOrder, Comment
from django.contrib import auth
from dinomania.forms import CommentForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, HttpResponseRedirect


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class MainView(ListView):
    template_name = "index.html"
    model = New
    queryset = New.objects.order_by("time").reverse()[:3]


class NewsView(ListView):
    template_name = "news.html"
    model = New
    queryset = New.objects.all().order_by("time").reverse()
    paginate_by = 3


class SortedNews(ListView):
    template_name = "news.html"
    paginate_by = 3
    model = New
    def get(self, request, *args, **kwargs):
        self.object_list = New.objects.all().order_by("time").reverse(
        ) if request.GET.get('reversed') else New.objects.all().order_by("time")
        context = super().get_context_data()
        return self.render_to_response(context)

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
    comment_form = CommentForm
    template_name = "news_detail.html"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        print(kwargs)
        context["comments"] = Comment.objects.all().filter(about = kwargs['pk'])
        context['comment_form'] = self.comment_form
        return self.render_to_response(context)


@login_required
@require_http_methods(["POST"])
def add_comment(request, pk):

    form = CommentForm(request.POST)
    news = get_object_or_404(New, pk=pk)

    if form.is_valid():
        if form.is_valid():
            comment = Comment()
            comment.path = []
            comment.about = news
            comment.author_id = auth.get_user(request)
            comment.content = request.POST.get('content')
            comment.save()

    return HttpResponseRedirect('/news/'+ pk)

class BooksDetail(DetailView):
    model = Book
    template_name = "books_detail.html"

class DinoDetail(DetailView):
    model = Dino
    template_name = "dino_detail.html"



#Ниже не подключенные но работающие функции

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

