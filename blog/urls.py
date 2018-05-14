from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/', views.blog),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^search/$', views.search),
    url(r'^search/search/', views.search_for),
    # url(r'^photo/',views.photo),
]
