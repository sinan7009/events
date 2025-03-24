
from django.urls import path, include
from events import views

urlpatterns = [
    path('', views.home , name= 'home'),
    path('<int:year>/<str:month>', views.home , name= 'home'),
    path('events',views.all_events, name= 'list_events'),
    path('add_venue', views.add_venue, name="add_venue"),
    ]