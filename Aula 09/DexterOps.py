#!/usr/bin/python

from Module.GitLabModule import GitLabModule
from Module.JenkinsModule import JenkinsModule
from Module.DockerModule import DockerModule
import json

class DeployTool():
	def __init__(self):
		pass

	def make(self):
		jm = JenkinsModule()
		gm = GitLabModule()
		dm = DockerModule()

		with open("application.json", "r") as f:
			j = json.loads(f.read())
			gm.createProject(j.get("application"))
			for d in j.get("developers"):
				gm.createUser(d.split("@")[0],d)
			gm.addProjectMember(j.get("application"), d)
			gm.addWebHook(j.get("application"), "http://jenkins.dexter.com.br:8080/gitlab/build_now")

			jm.createJob(j.get("application"), gm.getProjectRepo(j.get("application")))
			dm.createContainer(j.get("application"))
			dm.startContainer(j.get("application"))



if __name__ == '__main__':
	dt = DeployTool()
	dt.make()

