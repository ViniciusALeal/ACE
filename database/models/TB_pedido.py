"""
ID_pedido
email
score_total
"""
from peewee import *
from database.database import *


class tb_pedido(Model):
    email = CharField(unique=True)
    score_total = DecimalField()
    
