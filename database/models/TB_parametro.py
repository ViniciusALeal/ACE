"""
ID_parametro
fk_parametro_parametro
fk_tb_parametro
"""
from peewee import *
from database.database import *
from database.models.parametro import *
from database.models.TB_pedido import *

class tb_parametro(Model):
    parametro = ForeignKeyField(parametro, backref="Parametro")
    pedido = ForeignKeyField(tb_pedido, backref= 'Pedido')