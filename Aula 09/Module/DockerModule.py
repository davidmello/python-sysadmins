#!/usr/bin/python

from docker import Client
import json

class DockerModule():
	def __init__(self):
		self.cli = Client(base_url = "tcp://192.168.0.2:2376",version="auto")


	def createContainer(self, name):
		container = self.cli.create_container(image="ubuntu",
											  command="/bin/bash",
											  detach=True,
											  name=name,
											  tty=True,
											  stdin_open=True)


	def startContainer(self, container):
		help(self.cli)
		container = [ c.get("id") for c in self.cli.container(all=True) if min(c.get("Names") == "/" + container) ]
		self.cli.start_container(container=min(container))
		print "[+] Endereco do container %s" % (self.cli.inspect_container(min(container)).get("NetworkSettings").get("Networks").get("bridge").get("IPAddress"))

