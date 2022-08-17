from django.http import HttpResponseRedirect
from django.urls import path

from . import views

app_name = 'mixs'
urlpatterns = [
    path('', views.index, name='index'),
]
