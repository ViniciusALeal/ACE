from peewee import *
from database.database import db
from database.models.pedido import Pedido

class Geracao(Model):
    id = AutoField()  # PK
    genoma = CharField(null=False)
    id_pedido = ForeignKeyField(Pedido, backref='geracoes', on_delete='CASCADE')  # FK correta
    scores = CharField(null=True)
    done = BooleanField(default=False)  # Status de conclusão

    @property
    def pedido_nome(self):
        """ Retorna o nome do pedido relacionado sem armazenar no banco. """
        return self.id_pedido.pedido if self.id_pedido else None

    class Meta:
        database = db
        table_name = 'Geracao'
