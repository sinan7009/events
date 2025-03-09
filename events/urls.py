
from django.urls import path, include
from events import views

urlpatterns = [
    path('', views.home , name= 'home'),
    ]