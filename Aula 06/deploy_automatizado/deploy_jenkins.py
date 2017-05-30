#!/usr/bin/python

import jenkins
from lxml import etree

class JenkinsManager:

	def __init__(self):
		try:
			self.server = jenkins.Jenkins("http://jenkins.dexter.com.br:8080")
			print self.server.get_version()
		except Exception as e:
			print "Falha ao conectar: ", e
	

	def createJob(self):
		try:
			with open('job_template.xml','rw') as f:
					template = f.read().replace("git@gitlab.dexter.com.br","git@gitlab.dexter.com.br:devops/aplicacao-exemplo.git")

			
			root = etree.XML(template)
			for b in root.findall("builders"):
				builder = b
			# for b in root:
				# print str(b.tag) + ":" + str(b.text)
					# print b
			shell_step = etree.Element("hudson.tasks.Shell")
			comando = etree.Element("command")
			comando.text = " echo mensagem_teste"

			shell_step.append(comando)
			builder.append(shell_step)

			with open ("temp_template.xml","w") as f:
				f.write(etree.tostring(root))

			print self.server.create_job("Sardinha Template", etree.tostring(root))
		except Exception as e:
			print "Falhou ao criar Job: ", e


	def buildJob(self):
		try:
			# self.server.build_job("Sardinha")
			self.server.build_job("Sardinha",{"container":"cardume"})
		except Exception as e:
			print e


if __name__ == '__main__':
	j = JenkinsManager()
	# j.createJob()
	j.buildJob()