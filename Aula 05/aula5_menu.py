#!/usr/bin/python

from docker import Client
import json

heydoc = Client(base_url="tcp://192.168.0.2:2376",version="auto")
stay_on_menu = True

def menu():
	try:
		menu = " 1 - Listar os containers que estao rodando \n \
2 - Listar todos os containers \n \
3 - Criar container \n \
4 - Start container \n \
5 - Stop container \n \
6 - Remover container \n \
7 - Executar comando \n \
8 - Inspect container \n \
9 - Sair do sistema"
		print menu
		opcao = raw_input("Digite a opcao desejada: ")
		return int(opcao)
	except Exception as e:
		print "Error: %s" % e

def show_containers(todos=False):
	for c in heydoc.containers(todos):
		name = str(c.get("Names"))
		ids = c.get("Id")
		print "ID: %s | Name: %s" % (ids, name)


while stay_on_menu == True:
	resposta_menu = menu()
	try: 
		if resposta_menu == 1:
			show_containers()
		elif resposta_menu == 2:
			for c in heydoc.containers(all=True):
				name = str(c.get("Names"))
				ids = c.get("Id")
				print "ID: %s | Name: %s" % (ids, name)
		elif resposta_menu == 3:
			for c in heydoc.containers(all=True):
				name = str(c.get("Names"))
				ids = c.get("Id")
				print "ID: %s | Name: %s" % (ids, name)
			nome_novo_container = raw_input("Digite um nome para o novo container: ")
			imagem_baseada = raw_input("Digite a imagem que gostaria de se basear")
			heydoc.create_container(image=imagem_baseada,name=nome_novo_container,command="/bin/bash",tty=True)
		elif resposta_menu == 4:
			for c in heydoc.containers(all=True):
				name = str(c.get("Names"))
				ids = c.get("Id")
				print "ID: %s | Name: %s" % (ids, name)
			id_container = raw_input("Digite o ID do container: ")
			heydoc.start(id_container)
			print "Container vai ser iniciado"
		elif resposta_menu == 5:
			show_containers()
			id_container = raw_input("Desligar container ID: ")
			heydoc.stop(id_container)
		elif resposta_menu == 6:
			print "Nao quero remover containers"
		elif resposta_menu == 7:
			show_containers()
			container = raw_input("Em qual container deseja executar o comando: ")
			comando = raw_input("Qual comando deseja executar ?: ")
			create = heydoc.exec_create(container,comando)
			heydoc.exec_start(create.get("Id"))
		elif resposta_menu == 8:
			print " TESTE"
			for c in heydoc.containers(all=True):
				name = str(c.get("Names"))
				ids = c.get("Id")
				print "ID: %s | Name: %s" % (ids, name)
			numero_container = raw_input("Digite o ID do container: ")
			print json.dumps(heydoc.inspect_container( numero_container ), indent=4, sort_keys=True)
		elif resposta_menu == 9:
			stay_on_menu = False
	except Exception as e:
		print "Error: %s" % e
