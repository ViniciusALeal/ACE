
from routes.home import home
from routes.sobre import sobre
from routes.documentacao import documentacao
from routes.pedido import pedido
from database.models.pedido import Pedido
from database.models.geracao import Geracao
from database.database import db

def configure_app(app):
    configure_route(app)
    configure_db()

    
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
        db.create_tables([Pedido,Geracao], safe=True)
    except Exception as e:
        print(f"Erro ao configurar o banco de dados: {e}")