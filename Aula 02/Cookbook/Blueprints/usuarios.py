#!/usr/bin/python

from flask import Blueprint,jsonify,request
from Model import Usuarios
import json

usuarios = Blueprint("usuarios", __name__)

@usuarios.route("/usuarios/", methods=["GET"])
def index_usuarios():
	usuarios = json.loads(Usuarios.objects.all().to_json())
	return jsonify({"usuarios":usuarios})

@usuarios.route("/usuarios/", methods=["POST"])
def inserir_usuarios():
	dados = request.get_json()
	try:
		u = Usuarios()
		for key in dados.keys():
			setattr(u,key,dados[key])
		u.save()
		return jsonify({"message": "Usuario cadastrado som sucesso"})
	except Exception as e:
		return jsonify({"message":"Falha ao cadastrar %s" % e })


# @usuarios.route("/usuarios/<id>/", methods=["GET"])
# def busca_usuarios(id):
# 	u = Usuarios.

@usuarios.route("/usuarios/delete/<id>", methods=["DELETE"])
def deletar_usuario(id):
	u = Usuarios.objects(id=id)
	u.delete()
	data = {"message":"usuario removido com sucesso"}
	return jsonify(data)


@usuarios.route("/usuarios/<id>", methods=["PUT"])	
def atualizar_usuario(id):
	dados = request.get_json()
	u = Usuarios.objects(id=id).first()
	for key in dados.keys():
		setattr(u,key,dados[key])
	u.save()
	data = {"message":"usuario atualizado com sucesso"}
	return jsonify(data)