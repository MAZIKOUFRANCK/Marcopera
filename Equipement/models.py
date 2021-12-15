""" -- 
    -- Nom du document : views.py
    -- Nom du redaction : Franck Souverain MAZIKOU as ANÜBIS 👽
    -- Date de redaction : 10/12/2021
-- """

# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.db import models

# -- définition des classes modèles -- #
class Equipement(models.Model):
    # -- docstring de la classe Equipement -- #
    """
        -- Cette classe représente la table des équipements dans la base de 
        -- Données Marcopera
    """

    # -- mise en place des attributs de la classe Équipement -- #
    nom = models.CharField(max_length = 75, null =  False)
    description = models.TextField(null = False)
    image = models.ImageField(null = False, upload_to = 'imagesEquipements/')
    datePublication = models.DateTimeField(auto_now = True, null = False)

    # -- mise en place de la methode __str__ -- #
    def __str__(self):
        return f"Titre équipement : {self.nom} - Date publication : {self.datePublication}"
