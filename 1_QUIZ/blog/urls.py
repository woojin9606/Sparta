from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.view_main, name='main'),
    path('new/', views.create_article, name='new')
]