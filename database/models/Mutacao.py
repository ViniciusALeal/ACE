"""
original
mutante
ID_Mutacao
"""
from peewee import *
from database.database import *

class mutacao(Model):
    Original = TextField()
    Mutante = TextField()