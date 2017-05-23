#!/usr/bin/python

import requests
import json

# codigo = str(input("Codigo do usuario: "))
# 
# print ("http://0.0.0.0:5000/usuarios/%s/" % codigo )
# banana =  json.loads(requests.get("http://0.0.0.0:5000/usuarios/%s/" % codigo )._content)



# POST
banana 	= json.dumps({"nome":"valda","email":"valda@4linux.com.br"})
cabecalho   = {'content-type':'application/json'}

print requests.post("http://0.0.0.0:5000/usuarios/",data=banana,headers=cabecalho)._content

# PUT
banana 	= json.dumps({"nome":"vanda","email":"vanda@4linux.com.br"})
print requests.put("http://0.0.0.0:5000/usuarios/8/",data=banana,headers=cabecalho)._content

# DELETE
print requests.delete("http://0.0.0.0:5000/usuarios/8/",data=banana,headers=cabecalho)._content


# # GET
banana =  json.loads(requests.get("http://0.0.0.0:5000/usuarios/" )._content)
print banana
# for b in banana.get("usuarios"):
# 	print b.get("email") + "    \t" + b.get("nome")