#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask,jsonify,render_template
import json
from Blueprints.usuarios import usuarios
from Blueprints.Model import Usuarios



# from funcionarios import funcionarios

app = Flask(__name__)

app.register_blueprint(usuarios)

if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0",port=3000)