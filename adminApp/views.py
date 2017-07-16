from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User
from usermanagmentapp.forms import RegForm, UserChangeForm
from dinomania.forms import NewsForm, DinoForm, BookForm, AutorForm, ResursForm
from dinomania.models import New, Dino, Book, Autor


# доступ у админке только суперпользователю
# @user_passes_test(lambda u: u.is_superuser)

class News_admin(ListView):
    template_name = "other_admin.html"
    model = New
    paginate_by = 24

class Dino_admin(News_admin):    
    model = Dino
    
class New_del(DeleteView):
    model = New
    success_url = '/madmin/news/'
    template_name = 'confirm_delete.html'

class Dino_del(New_del):
    model = Dino
    success_url = '/madmin/dino/'

class NewsUpdateView(UpdateView):
    model = New
    template_name = 'admin_update.html'
    fields = ('__all__')
    success_url = '/admin/news/'

class DinoUpdateView(NewsUpdateView):
    model = Dino
    success_url = '/admin/dino/'

class NewsCreateView(CreateView):
    model = New
    template_name = 'admin_create.html'
    fields = ('__all__')
    success_url = '/admin/news/'

class DinoCreateView(NewsUpdateView):
    model = Dino
    success_url = '/admin/dino/'


def madmin_page(request):
    users = User.objects.all()
    user_form = RegForm()

    return render(request, 'admin_page.html', {'users': users, 'form': user_form})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/madmin')



def get_user_form(request, user_id):
    """
    Возвращает заполненную форму для редактирования Пользователя(User) с заданным user_id
    """
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        
        user_form = RegForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc_regform.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404
         

def create_user(request, user_id=None):
    """
    Создает Пользователя(User)
    Или редактирует существующего, если указан  user_id
    """
    if request.is_ajax():       
        if not user_id:        
            user = RegForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc_users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404

