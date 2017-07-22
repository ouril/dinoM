"""dino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from adminApp.views import User_del,  \
    News_admin, New_del, NewsUpdateView, \
    NewsCreateView, User_admin, UserUpdateView, UserCreateView


urlpatterns = [
    url(r'^$', login_required(User_admin.as_view()), name='mad'),
    url(r'^delete/user/(?P<pk>\d+)$', login_required(User_del.as_view())),
    url(r'^get_user_form/(?P<pk>\d+)$', login_required(UserUpdateView.as_view())),
    url(r'^create/user/$', login_required(UserCreateView.as_view()), name='create_us'),
    url(r'^news$', login_required(News_admin.as_view()), name='news_adm'),
    url(r'^create/news$', login_required(NewsCreateView.as_view()), name='create'),
    url(r'^delete/news/(?P<pk>\d+)$',login_required(New_del.as_view()), name='delete'),
    url(r'^update/news/(?P<pk>\d+)$', login_required(NewsUpdateView.as_view()), name='update')
]
