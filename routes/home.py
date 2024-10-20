# routes/home.py
from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def hello_world():
    return render_template('home/index.html')

@home.route('/demo')
def demo():
    return 'This is a demo route.'
