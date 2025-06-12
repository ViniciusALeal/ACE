# models/pedido.py
from peewee import *
from database.database import db

class Pedido(Model):
    id = AutoField()  # PK
    pedido = CharField(null=False)  
    email = CharField(null=True)  

    class Meta:
        database = db
        table_name = 'Pedido'
