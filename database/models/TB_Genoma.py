"""

geracao
score_genoma
tipo 
fk_tb_pedido

"""

from peewee import *
from database.database import *
from database.models.TB_pedido import*

class tb_genoma(Model):
    pedido = ForeignKeyField(tb_pedido, backref= 'Pedido')
    geracao = DecimalField(null=False)
    tipo = CharField(null=False)
    score_genoma= DecimalField