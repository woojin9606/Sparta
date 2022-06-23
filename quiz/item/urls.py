from django.urls import path, include
from item import views

urlpatterns = [
    # user/
    path('', views.ItemView.as_view()),
]