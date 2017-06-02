#!/usr/bin/python

import ConfigParser
import json
import os
import requests


class GitLabModule():
	def __init__(self):
		config = ConfigParser.ConfigParser()
		config.read(os.path.dirname(os.path.abspath(__file__))+"/../config.cfg")
		self.server = config.get("gitlab","server")
		self.token  = config.get("gitlab","token")	


	def make_post(self,url,data):
		response = requests.post("http://%s/api/v3/%s?private_token=%s" % (self.server,url,self.token), data=data)
		# response = "http://%s/api/v3/%s?private_token=%s" % (self.server,url,self.token)
		return response

	def make_get(self,url,data):
		response = requests.get("http://%s/api/v3/%s/%s?private_token=%s" % (self.server,url,data,self.token))
		return response

	def createUser(self,name,email):
		resource = "users"
		data = {"name":name, 
				"username": name,
				"email": email,
				"password": "4linux123",
				"confirm": False
				}
		response = self.make_post(resource,data)
		if response.status_code == 201:
			print "Usuario criado com sucesso"
		else:
			print "Falhou ao criar usuario %s" % response.text
	
	def createProject(self, application):
		response = self.make_post("projects", {"name":application})
		# print response.status_code
		if response.status_code == 201:
			print "Projecto criado com sucesso"
		else:
			print "Problema ao criar projeto %s" % response.text

	def addProjectMember(self,project,member):
		response = self.make_get("projects", "/all")
		project_id  = min([ r.get("id") for r in response.json() if r.get("name") == project ])

		response = self.make_get("users", "")
		user_id  = min([ r.get("id") for r in response.json() if r.get("email") == member ])
		print user_id
		data = {"id": project_id, "user_id": user_id, "access_level": 10}
		response = self.make_post("projects/%s/members" % project_id, data)
		if response.status_code == 201:
			print "Membro adicionado com sucesso"
		else:
			print "Falha ao adicionar Membro %s" % response.text


	def addWebHook(self, project, url):
		response = self.make_get("projects", "/all")
		project_id = min([r.get("id") for r in response.json() if r.get("name") == project])
		data = {"url": url , "push_events": True}
		response = self.make_post("projects/%s/hooks" % project_id, data)
		if response.status_code == 201:
			print "Hook adicionado com sucesso"


	def getProjectRepo(self, project):
		response = self.make_get("projects", "/all")
		project = min([r.get("ssh_url_to_repo") for r in response.json() if r.get("name") == project ])

		if project:
			return str(project)
		else:
			print "Projeto nao existe"