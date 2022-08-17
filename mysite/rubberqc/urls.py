from django.urls import path

from . import views

app_name = 'rubberqc'
urlpatterns = [
    path('', views.index, name='index'),
]
