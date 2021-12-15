""" -- 
    -- Nom du document : views.py
    -- Nom du redaction : Franck Souverain MAZIKOU as ANÜBIS 👽
    -- Date de redaction : 12/12/2021
-- """

# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.db import models

# -- définition des classes modèles -- #
class Internaute(models.Model):
    # -- docstring de la classe Internaute -- #
    """
        -- Cette classe représente la table des internautes dans la base de 
        -- Données Marcopera
    """

    # -- mise en place des attributs de la classe internautes -- #
    nom = models.CharField(max_length = 75, null =  False)
    numeroTelephone = models.CharField(max_length = 75, null = False)
    adresseMail = models.EmailField(null = False)
    dateCreation = models.DateTimeField(auto_now = True, null = False)

    # -- mise en place de la methode __str__ -- #
    def __str__(self):
        return f"Nom internaute : {self.nom} - Date création : {self.dateCreation}"

class Message(models.Model):
    # -- docstring de la classe Message -- #
    """
        -- Cette classe représente la table des message dans la base de 
        -- Données Marcopera
    """

    # -- mise en place des attributs de la classe messages -- #
    sujet = models.CharField(max_length = 75, null =  False)
    message = models.TextField(null =  False)
    idInternaute = models.ForeignKey(Internaute, null = True, on_delete = models.SET_NULL)
    dateEnvoi = models.DateTimeField(auto_now = True, null = False)

    # -- mise en place de la methode __str__ -- #
    def __str__(self):
        return f"Sujet : {self.sujet} - Message : {self.message} - Date : {self.dateEnvoi}"
