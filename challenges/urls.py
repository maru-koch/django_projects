
from django.urls import path
from . import views

urlpatterns = [
    #: to reference the app path specified in the project url.py
    #: leave the url here empty

    path('', views.index, name = "index"),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name = "monthly_challenge")    
]