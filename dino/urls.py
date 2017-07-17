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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from adminApp.views import madmin_page, delete_user, get_user_form, create_user, \
    News_admin, New_del, NewsUpdateView, \
    NewsCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('dinomania.urls')),
    url(r'^user/', include('usermanagmentapp.urls'))

]

urlpatterns += {
    url(r'^madmin/$', madmin_page, name='mad'),
    url(r'^madmin/delete/user/(\d+)$', delete_user),
    url(r'^madmin/get_user_form/(\d+)$', get_user_form),
    url(r'^madmin/create/user/(\d*)$', create_user),
    url(r'^madmin/news/', News_admin.as_view(), name='news'),
    url(r'^madmin/create/news$', NewsCreateView.as_view(), name='create'),
    url(r'^madmin/delete/news/(?P<pk>\d+)$', New_del.as_view(), name='delete'),
    url(r'^madmin/update/news/(?P<pk>\d+)$', NewsUpdateView.as_view(), name='update')
}


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
