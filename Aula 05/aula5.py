#!/usr/bin/python

from docker import Client

heydoc = Client(base_url="tcp://192.168.0.2:2376",version="auto")

# listar containers iniciados
for c in heydoc.containers():
	cont = c.get("Names")

print heydoc.inspect_container("pudim")

# cria um container de acordo com uma imagem
heydoc.create_container(image="debian",name="sexta",command="/bin/bash",tty=True)

# inicia o container
heydoc.start(container="sexta")

# stop no container
# heydoc.stop(container="sexta")

# remove container
# heydoc.remove_container(container="sexta")

create = heydoc.exec_create("sexta","apt-get update")

heydoc.exec_start(create.get("Id"))