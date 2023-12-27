from django.urls import path
from . import views

# URLConf -> URL Configuration
urlpatterns = [
    path('hello/', views.say_hello)
]

