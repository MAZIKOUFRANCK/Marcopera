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

# -- définition des urls de l'application Equipement -- #
urlpatterns = [
    path('', views.equipement, name = "equipement"),
    path('rechercheEquipement/', views.rechercheEquipement, name = "rechercheEquipement"),
    path('rechercheEquipementCle/<str:motCle>/', views.rechercheEquipementCle, name = "rechercheEquipementCle"),
]
