from django.urls import path, re_path
from .import views

app_name = 'programs'


urlpatterns = [
    # /Program/
    path('', views.index, name='index'),

    # Program/id
    re_path(r'^(?P<program_id>[0-9]+)/$', views.detail, name='detail')

]
2