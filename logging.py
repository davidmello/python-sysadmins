#!/usr/bin/python

import logging


class Logging():
	def __init__(self):
		try: 
			logging.basicConfig(filename="logs/dexter.logs",level=logging.INFO,format="%(asctime)s %(message)s", datefmt="[ %d/%m/%Y - %H:%M:%S]")
		except Exception as e:
			print "Erro ao escrever no Log ", e