from flask import render_template, Blueprint
    
documentacao=Blueprint('documentacao',__name__)
@documentacao.route('/documentacao')
def documentacao_route():
    return render_template('documentacao.html')
