from django.urls import path

from . import views

app_name = 'formtest'
urlpatterns = [
    path('', views.get_name, name='get_name'),
]
