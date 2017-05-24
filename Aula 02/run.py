#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,jsonify
from grupos import grupos

app = Flask(__name__)

app.register_blueprint(grupos)

@app.route("/")
def index():
	data = {"messages":"Hello... universe!"}
	return jsonify(data)

@app.route("/usuarios/", methods=["GET"])
def index_usuarios():
	data = {"message":"Hello insect..."}
	return jsonify(data)
	# return render_template("index.html")

@app.route("/usuarios/",methods=["POST"])
def insere_usuarios_especifico():
	data = {"message":"Hello insect... What do you want with %s?..."}
	return jsonify(data)

@app.route("/usuarios/<int:id>/",methods=["GET"])
def lista_usuarios_especificos(id):
	data = {"message":"Hello insect... What do you want with %s?..." % id}
	return jsonify(data)

@app.route("/usuarios/<int:id>/<nome>/",methods=["PUT"])
def atualiza_usuarios_especificos(id,nome):
	data = {"message":"Insect! Why you changed the name to %s ?" % nome}
	return jsonify(data)

@app.route("/admin/")
def admin():
	data = {"message":"Hello my lord! How may I serve you today 	?"}
	return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0",port=3000)