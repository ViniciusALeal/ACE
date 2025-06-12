from flask import render_template, Blueprint
    
sobre=Blueprint('sobre',__name__)
@sobre.route('/sobre')
def sobre_route():
    return render_template('sobre.html')
