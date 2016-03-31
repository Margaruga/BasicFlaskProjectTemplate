
# -*- coding: utf-8 -*-


from flask import render_template, send_from_directory
from . import main_blueprint

@main_blueprint.route('/')
def index():
    return render_template('index.html')
    
@main_blueprint.route('/<name>')
def hello(name):
    return '<h1> Hello {name} </h1>'.format(name=name)


