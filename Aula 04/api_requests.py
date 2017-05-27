#!/usr/bin/python

import requests
import json

token = "1irgLViWqybuM19dhAgQ"
# url = "http://gitlab.dexter.com.br/api/v3/%s?private_token=%s" % (recurso,token)

# insere usuario
def cria_usuario(url,token,recurso,nome,password,email,username):
	url = "http://gitlab.dexter.com.br/api/v3/%s?private_token=%s" % (recurso,token)
	recurso = "users"
	usuario = {"name":nome,"password":password,"email":email,"username":username}
	# response = json.loads(requests.post(url,data=usuario)._content)
	response = requests.post(url,data=usuario).status_code
	return response
	
def lista_usuarios(recurso):
	# faz request de informacoes
	url = "http://gitlab.dexter.com.br/api/v3/%s?private_token=%s" % (recurso,token)
	a = ''
	response = json.loads(requests.get(url)._content)
	# Exibe a listagem de usuarios
	# for r in response:
	# 	a = a + r.get("username") + "\n"
	# return a
	return response

def lista_projetos(recursos,token):
	# faz request de informacoes
	url = "http://gitlab.dexter.com.br/api/v3/%s?private_token=%s" % (recursos,token)
	a = ''
	response = json.loads(requests.get(url)._content)
	# Exibe a listagem de usuarios
	# for r in response:
	# 	a = a + r.get("name") + "\n"
	# return a
	return response

def add_project_members(project_id,user_id):
	token = "1irgLViWqybuM19dhAgQ"
	url = "http://gitlab.dexter.com.br/api/v3/projects/%s/members/?private_token=%s" % (recurso,token)
	membro = { "project_id": project_id,"user_id":user_id, "access_level":30 }
	response = json.loads(requests.post(url,data=membro)._content)
	return response


def addprojecthook(project_id,hook_url):
	url = "http://gitlab.dexter.com.br/api/v3/projects/%s/hooks?private_token=%s" % (project_id,token)
	hook = {"url":hook_url,"push_events":True}

	response = json.loads(requests.post(url,data=hook)._content)

if __name__ == '__main__':
	# x=0
	# while x < 10: 

	# 	cria_usuario(url,token,recurso,"David%s" % x,"4linux123","david.hasson%s@gmail.com" % x ,"david.hasson%s" % x)
	# 	x=x+1

	# print lista_projetos("projects", token)
	# print lista_usuarios("users")
	# add_project_members(,)

	# user_id = [u for u in lista_usuarios("users") if u.get("username") == "Davous"]
	projetos = lista_projetos("projects", "1irgLViWqybuM19dhAgQ")	
	usuarios = lista_usuarios("users")
	for u in usuarios:
		print u.get("username") + ":" + str(u.get("id"))

	for p in projetos:
		print p.get("name") + ":" + str(p.get("id"))

	addprojecthook(9,"http://jenkins:8080/hook")
		

	# print user_id
