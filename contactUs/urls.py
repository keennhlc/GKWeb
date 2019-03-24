from django.urls import path
from .import views

app_name = 'contactUs'

urlpatterns = [
    path('', views.contact_create_view, name='contact_create_view'),
]
