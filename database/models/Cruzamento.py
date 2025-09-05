"""
fk_familia_familia_pk
ID_cruzamento

"""
from peewee import *
from database.database import *
from database.models.familia import *

class cruzamento(Model):
    familia = ForeignKeyField (familia)
    