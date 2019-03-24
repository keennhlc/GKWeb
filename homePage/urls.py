from django.urls import path, re_path
from .import views

app_name = 'homePage'

urlpatterns = [
     path('', views.index, name='index'),


     re_path(r'^News/(?P<new_id>[0-9]+)/$', views.news_detail, name='news_detail'),

     re_path(r'^slider/(?P<slider_id>[0-9]+)/$', views.slider_detail, name='slider_detail')
]


"""
    re_path(r'^news/(?P<new_id>[0-9]+)/$', views.news_detail, name='news_detail'),

    re_path(r'^slider/(?P<slider_id>[0-9]+)/$', views.slider_detail, name='slider_detail'),"""
