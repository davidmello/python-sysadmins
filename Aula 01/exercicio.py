#!/usr/bin/python

import requests
import json

kbcalho = {'content-type':'application/json'}

email = raw_input("Digite um email: ")

banana = json.loads(requests.get("http://0.0.0.0:5000/usuarios/",headers=kbcalho).content)

for b in banana.get("usuarios"):
	if b.get("email") == email:
		print b.get("nome")