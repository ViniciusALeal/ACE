from flask import render_template, Blueprint
    
home=Blueprint('home',__name__)
@home.route('/')
def home_route():
    return render_template('index.html')
