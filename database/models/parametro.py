"""
parametro_pk
valor

"""
from peewee import *
from database.database import *

class parametro(Model):
    varparametro = TextField ()
    valor = TextField()