#!/usr/bin/python

import jenkins
import os
import json
import lxml.etree as etree
import ConfigParser

class JenkinsModule():

	def __init__(self):
		config = ConfigParser.ConfigParser()
		config.read(os.path.dirname(os.path.abspath(__file__))+"/../config.cfg")
		self.server = jenkins.Jenkins(config.get("jenkins", "server")+":8080")


	def createJob(self, application, repo):
		with open(os.path.dirname(os.path.abspath(__file__))+"/../Templates/job.xml", "r") as f:
			job_xml = f.read().replace("REPO",repo)
			xml = etree.tostring(self.generateJobSteps(job_xml,application))
			self.server.create_job(application,xml)


	def generateJobSteps(self,xml,application):
		with open(os.path.dirname(os.path.abspath(__file__))+"/../application.json") as f:
			deploy = json.loads(f.read())
		root = etree.XML(xml)
		for b in root.findall("builders"):
			builder = b
		for c in deploy.get("deploy-sequence").get("commands"):
			command = etree.Element("command")
			command.text = "ssh forlinux@192.168.0.2 \"docker exec %s bash -c '%s' \"" % (application, c)
			step = etree.Element("hudson.task.Shell")
			step.append(command)
			builder.append(step)
			return root