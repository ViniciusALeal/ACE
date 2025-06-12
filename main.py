from flask import Flask
from config import configure_app

app = Flask(__name__)

# Configurar o app corretamente
configure_app(app)


if __name__ == '__main__':
    app.run(debug=True)
