from django.urls import path

from . import views

app_name = 'mixs_dup'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pp_id>/', views.detail, name='detail'),
    path('results/<int:pp_id>/', views.results_sheet, name='results_sheet'),
]
