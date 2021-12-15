""" -- 
    -- Nom du document : urls.py
    -- Nom du redaction : Franck Souverain MAZIKOU as ANÜBIS 👽
    -- Date de redaction : 10/12/2021
-- """

# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.contrib import admin
from .models import Equipement

# -- mise en place des registres -- #
admin.site.register(Equipement)

