from flask import Flask
from flask.ext.mongoengine import MongoEngine
import datetime
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {	"db":"dexter-api"	}

db = MongoEngine(app)

class Usuarios(db.Document):
	nome = db.StringField()
	email = db.StringField(unique=True)
	data_cadastro = db.DateTimeField(default=datetime.datetime.now)


class Grupos(db.Document):
	nome = db.StringField(unique=True)
	integrantes = db.ListField()


if __name__ == '__main__':
	u = Usuarios()
	u.nome = "Valda"
	u.email = "valda@4linux.com.br"
	u.save()
	g = Grupos()
	g.nome = "Banana"
	g.integrantes.append(u)
	g.save()
	print "Grupo / Usuario cadastrados com sucesso =)"