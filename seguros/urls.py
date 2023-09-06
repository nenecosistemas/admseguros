from django.urls import path
from seguros import views

urlpatterns = [
    path('', views.home),
    path('home',views.home),
    path('aseguradoform', views.aseguradoform),
    
]
