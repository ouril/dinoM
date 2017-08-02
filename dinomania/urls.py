from django.conf.urls import url
from dinomania.views import MainView, NewsView, BooksView, NewsDetail, BooksDetail, \
    DinoView, DinoDetail, SortedNews, add_comment

urlpatterns = [

    url(r'^$', MainView.as_view(), name='main'),
    url(r'^news$', NewsView.as_view(), name='news'),
    url(r'^news/sorted/$', SortedNews.as_view(), name='sort'),
    url(r'^comment/(?P<pk>\d+)/$', add_comment, name='add_comment'),
    url(r'^books/$', BooksView.as_view(), name='books'),
    url(r'^books/(?P<pk>\d+)/$', BooksDetail.as_view(), name='books_detail'),
    url(r'^dino/$', DinoView.as_view(), name='dino'),
    url(r'^dino/(?P<pk>\d+)/$', DinoDetail.as_view(), name='dino_detail'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetail.as_view(), name='news_detail')
]