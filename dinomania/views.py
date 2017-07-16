from django.shortcuts import render
from dinomania.models import New, Dino
from django.views.generic.list import ListView


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

