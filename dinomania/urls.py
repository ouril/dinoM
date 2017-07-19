from django.conf.urls import url
from dinomania.views import MainView, NewsView, BooksView, NewsDetail,sort_for_time

urlpatterns = [

    url(r'^$', MainView.as_view(), name='main'),
    url(r'^news$', NewsView.as_view(), name='news'),
    url(r'^news/sorted/$', sort_for_time, name='sort'),
    url(r'^books/$', BooksView.as_view(), name='books'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetail.as_view(), name='news_detail')
]