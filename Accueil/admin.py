""" -- 
    -- Nom du document : urls.py
    -- Nom du redaction : Franck Souverain MAZIKOU as ANÜBIS 👽
    -- Date de redaction : 12/12/2021
-- """

# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.contrib import admin
from .models import Internaute, Message

# -- mise en place des registres -- #
admin.site.register(Internaute)
admin.site.register(Message)

