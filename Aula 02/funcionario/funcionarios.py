#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,jsonify
import json

funcionarios = Blueprint('funcionarios', __name__)

@funcionarios.route("/funcionarios/")
def lista_funcionarios():
	json_data = open('banco.json').read()
	# with open('banco.json','r') as f:
	# 	arquivo_json = json.loads(f.read())
	# total = json.dumps(arquivo_json)
	arquivo_json = json.loads(json_data)
	a = " "
	for f in arquivo_json:
		a = a + " " + f["nome"] + "<br />"
	return a

@funcionarios.route("/funcionarios/<id>")
def lista_funcionario(id)
	json_data = open('banco.json').read()
	# with open('banco.json','r') as f:
	# 	arquivo_json = json.loads(f.read())
	# total = json.dumps(arquivo_json)
	arquivo_json = json.loads(json_data)
	a = " "
	for f in arquivo_json:
		if f["id"] == id:
			return f["nome"]
		
		# for funciona in arquivo_json:
		# 	return funciona["id"]
	