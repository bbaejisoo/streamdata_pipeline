from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('document/', views.document, name='document'),
    path('create_chart/', views.create_chart, name='create_chart'),
]
