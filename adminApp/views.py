from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from usermanagmentapp.forms import RegForm
from django.contrib.auth.decorators import user_passes_test


# доступ у админке только суперпользователю
# @user_passes_test(lambda u: u.is_superuser)
def madmin_page(request):
    users = User.objects.all()
    user_form = RegForm()

    return render(request, 'admin_page.html', {'users': users, 'form': user_form})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin')