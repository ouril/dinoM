from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect

from django.contrib.auth.models import User
from usermanagmentapp.forms import RegForm, UserChangeForm
from dinomania.forms import NewsForm, DinoForm, BookForm, AutorForm, ResursForm
from dinomania.models import New, Dino


# доступ у админке только суперпользователю
# @user_passes_test(lambda u: u.is_superuser)
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
        print('user_id = ', user_id)
        print("good")      
        if not user_id:   
            print("good")      
            user = RegForm(request.POST)
        else:
            print("good for change") 
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            print("good validation")
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc_users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404

def admin_dino(request):
    dino = Dino.objects.all()
    dino_form = DinoForm()
    return render(request, 'admin_page.html', {'users': dino, 'form': dino_form})