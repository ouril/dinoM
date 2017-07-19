from django.conf.urls import url
from dinomania.views import MainView, NewsView, BooksView, NewsDetail,sort_for_time,BooksDetail, \
    DinoView, DinoDetail

urlpatterns = [

    url(r'^$', MainView.as_view(), name='main'),
    url(r'^news$', NewsView.as_view(), name='news'),
    url(r'^news/sorted/$', sort_for_time, name='sort'),
    url(r'^books/$', BooksView.as_view(), name='books'),
    url(r'^books/(?P<pk>\d+)/$', BooksDetail.as_view(), name='books_detail'),
    url(r'^dino/$', DinoView.as_view(), name='dino'),
    url(r'^dino/(?P<pk>\d+)/$', DinoDetail.as_view(), name='dino_detail'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetail.as_view(), name='news_detail')
]