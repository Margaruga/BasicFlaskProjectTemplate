
# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

from .main import main_blueprint
app.register_blueprint(main_blueprint)

@app.route('/static/<folder>/<name>')
def serve(folder, name):
    '''
    Only for developing purpose
    '''
    dirname = os.path.dirname(__file__)
    return send_from_directory(os.path.join(dirname, 'static', folder), filename=name)
