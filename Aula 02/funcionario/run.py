#!/usr/bin/python
# -*- coding: utf-8 -*-

# /funcionarios - lista todos os funcionarios cadastrados
# /funcionarios/1 - lista informacoes sobre um funcionario
# /funcionarios/1/dependentes/ deve listar todos os dependentes
# /funcionarios/1/dependentesse for feito um post, deve incluir um novo dependente
# /funcionarios/1/dependentes/1 deve mostrar informacoes sobre um dependente
# /funcionarios/1/dependentes/1 delete deve excluir informacoes sobre um dependente
 


from flask import Flask,jsonify
import json
# from funcionarios import funcionarios

app = Flask(__name__)

# app.register_blueprint(funcionarios)

@app.route("/funcionarios/")
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

@app.route("/funcionarios/<int:id>/")
def lista_funcionario(id):
	json_data = open('banco.json').read()
	arquivo_json = json.loads(json_data)
	a = " "
	for f in arquivo_json:
		if f["id"] == id:
			return f["nome"]
		
@app.route("/funcionarios/<int:id>/dependentes/")
def lista_dependentes_funcionario(id):
	json_data = open('banco.json').read()
	arquivo_json = json.loads(json_data)
	a = " "
	for f in arquivo_json:
		if f["id"] == id:
			b = " "
			for d in f["dependentes"]:
				b = b + " " + d["nome"] + "<br />"
			return b
				
@app.route("/funcionarios/<int:id>/dependentes/<nome>/<idade>/",methods=["POST"])
def insere_dependentes_funcionario(id,nome,idade):
	# arquivo_aberto = json.loads(open('banco.json','r+').read())
	arquivo_aberto = open('banco.json','r+').read()

	arquivo_json = json.loads(arquivo_aberto)

	# return help(id)
	# return str(adicionar)
	adicionar = json.dumps({"nome": nome, "idade": idade})

	
	for f in arquivo_json:
		if f["id"] == id:
			f.append(json.loads(adicionar))
			
	# arquivo_aberto.write(f)
	return "	"


if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0",port=3000)