
from routes.home import home
from routes.sobre import sobre
from routes.documentacao import documentacao
from routes.pedido import pedido
from database.database import *
from database.models.TB_Script import *
from database.models.TB_pedido import *
from database.models.TB_parametro import*
from database.models.TB_Genoma import*
from database.models.simple import*
from database.models.parametro import*
from database.models.Cruzamento import*
from database.models.familia import *
from database.models.Mutacao import*


def configure_app(app):
    configure_route(app)
    configure_db

    
def configure_route(app):
    app.register_blueprint(home)
    app.register_blueprint(sobre)
    app.register_blueprint(documentacao)
    app.register_blueprint(pedido)

def configure_db():
    """Conecta ao banco de dados e cria as tabelas caso necessário."""
    try:
        db.connect()
        # Adicionar Item à lista de tabelas a serem criadas
        db.create_tables([TB_script,tb_pedido,tb_parametro,tb_parametro,simple,parametro,mutacao,familia,cruzamento], safe=True)
    except Exception as e:
        print(f"Erro ao configurar o banco de dados: {e}")