from django.urls import path
from . import views

urlpatterns = [
    #Aqui crean la URL de cada vista de esta app
    path('', views.control, name = 'control'),
]