from django.conf.urls import url
from dinomania.views import MainView, NewsView, BooksView, NewsDetail

urlpatterns = [

    url(r'^$', MainView.as_view(), name='main'),
    url(r'^news$', NewsView.as_view(), name='news'),
    url(r'^books$', BooksView.as_view(), name='books'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetail.as_view(), name='news_detail')
]