#!/usr/bin/python

from paramiko import SSHClient
import paramiko

class SSHModule:
	def __init__(self):
		try:
			self.server = "192.168.0.2"
			self.client = SSHClient()
			self.client.load_system_host_keys()
			self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.client.connect(hostname=self.server, username="forlinux", password="4linux")
		except Exception as e:
			print "Falhou ao conectar ao servidor", e


	def execCommand(self, cmd):
		try:
			# Estudar esta linha:
			stdin, stdout, stderr = self.client.exec_command(cmd)
			if stderr.channel.recv_exit_status() != 0:
				return sterr.read()
			else:
				return stdout.read()

		except Exception as e:
			print "Falhou ao executar comando: ", e
