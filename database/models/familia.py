"""
Familia_pk
genoma_A
genoma_B
Filho
"""
from peewee import *
from database.database import *

class familia(Model):
    genomaA = TextField ()
    genomaB = TextField()
    filho= TextField()