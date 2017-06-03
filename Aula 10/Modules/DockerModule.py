#!/usr/bin/python

from docker import Client
import json

class DockerModule():
	def __init__(self):
		try:
			self.client = Client(base_url = "tcp://192.168.0.2:2376",version="auto")
		except Exception as e:
			print "Falhou ao conectar no Docker %s", e


	def listContainers(self):
		container = self.client.container(all=True)
		return container
