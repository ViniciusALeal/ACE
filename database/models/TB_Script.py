""" 
script
Avaliação_Subjetiva
"""
from peewee import *
from database.database import *

class TB_script(Model):
    #peewee tem id de auto encremento automatico caso não encontrei varivael com o atributo primarykey = true
    script = TextField(unique=True)
    avaliacao=IntegerField()

    
    