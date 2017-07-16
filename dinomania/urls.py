from django.conf.urls import url
from dinomania.views import MainView, NewsView

urlpatterns = [

    url(r'^$', MainView.as_view(), name='main'),
    url(r'^news$', NewsView.as_view(), name='news')
]