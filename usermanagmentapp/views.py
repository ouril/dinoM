from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from usermanagmentapp.forms import RegForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})

    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def regis(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            print("good")
            print(form)
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'registration.html', {'form': form})
    return render(request, 'registration.html', {'form': RegForm()})
