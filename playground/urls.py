from django.urls import path
from . import views

# URLConf -> URL Configuration
urlpatterns = [
    path('', views.index),
    path('hello/', views.say_hello)
]

