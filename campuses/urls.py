from django.urls import path, re_path
from .import views


app_name = 'campuses'

urlpatterns = [
    path('', views.index, name='index'),

    re_path(r'^(?P<campus_id>[0-9]+)/$', views.detail, name='detail'),
]
