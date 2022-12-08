from django.urls import path
from .import views  

urlpatterns = [
    path('', views.enter, name='enter'),
    path('home', views.home, name='home')
]
