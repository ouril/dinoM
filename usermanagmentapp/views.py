from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404

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
