""" -- 
    -- Nom du document : urls.py
    -- Nom du redaction : Franck Souverain MAZIKOU as ANÜBIS 👽
    -- Date de redaction : 10/12/2021
-- """

# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.urls import path
from . import views

# -- définition des urls de l'application accueil -- #
urlpatterns = [
    path('', views.accueil, name = "accueil"),
    path('contacter/', views.contacter, name = "contacter"),
]
