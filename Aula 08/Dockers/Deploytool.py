#!/usr/bin/python

from Module.DexterBookParser import DexterBookParser
from Module.DexterModule import DexterModule
import argparse


class DeployTool:
	def __init__(self):
		try:
			self.parser = argparse.ArgumentParser()
			self.parser.add_argument('-i',help="Esta opcao indica o caminho do DexterBook que ira realizar o deploy")
		except Exception as e:
			print e

	def getArgs(self):
		return self.parser.parse_args()


	def make(self, deploy_params):
		try:
			d = DexterModule()
			d.create_container(deploy_params.get("application"))
			for c in deploy_params.get("deploy-sequence").get("commands"):
				print d.exec_command(deploy_params.get("application"),c)
		except Exception as e:
			print e


if __name__ == '__main__':
	dt = DeployTool()
	args = dt.getArgs()
	book = DexterBookParser(args.i)
	dt.make(book.get())
	# for i in book.get().get("deploy-sequence").get("commands"):
	# 	print i
	
	
	