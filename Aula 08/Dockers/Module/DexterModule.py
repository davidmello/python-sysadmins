#!/usr/bin/python

from docker import Client
from SSHModule import SSHModule

class DexterModule(SSHModule):

	def __init__(self):
		try:
			self.cli = Client(base_url="tcp://192.168.0.2:2376",version="auto")
			SSHModule.__init__(self)
		except Exception as e:
			print "Falha ao conectar ao servidor: ", e



	def create_container(self,name):
		try:
			print "[+] Creating container: ", name
			container = self.cli.create_container(	image="ubuntu", 
													name=name, 
													command="/bin/bash", 
													detach=True, 
													tty=True,
													stdin_open=True
												)
			self.cli.start(container=container.get("Id"))
		except Exception as e:
			print "Falha ao criar container: ", e


	def exec_command(self,container,cmd):
		try:
			print "[+] Running command: ", cmd
			command = "docker exec %s %s" % (container,cmd)
			print self.execCommand(command)
		except Exception as e:
			print "Falhou ao executar o comando:", e