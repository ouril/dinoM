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
from adminApp.views import madmin_page, delete_user, get_user_form, create_user, \
    News_admin, New_del, NewsUpdateView, \
    NewsCreateView



urlpatterns = {
    url(r'$', madmin_page, name='mad'),
    url(r'^delete/user/(\d+)/$', delete_user),
    url(r'^get_user_form/(\d+)/$', get_user_form),
    url(r'^create/user/(\d*)/$', create_user),
    url(r'news/', News_admin.as_view(), name='news_adm'),
    url(r'^create/news/$', NewsCreateView.as_view(), name='create'),
    url(r'^delete/news/(?P<pk>\d+)/$', New_del.as_view(), name='delete'),
    url(r'^update/news/(?P<pk>\d+)/$', NewsUpdateView.as_view(), name='update')
}


