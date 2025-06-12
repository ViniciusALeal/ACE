from flask import render_template, Blueprint
    
pedido=Blueprint('pedido',__name__)
@pedido.route('/pedido')
def pedido_route():
    return render_template('pedido.html')
