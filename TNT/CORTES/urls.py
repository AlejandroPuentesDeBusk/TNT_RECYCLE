from django . urls import path
from . import views

    #Aqui crean la URL de cada vista de esta app
urlpatterns =[ 
    path ('', views.cortes, name = 'cortes'),
]
