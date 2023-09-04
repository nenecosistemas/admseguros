from django.urls import path
from seguros import views

urlpatterns = [
    path('', views.home),
    
]
