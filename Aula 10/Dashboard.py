#!/usr/bin/python

from flask import Flask, render_template, request, jsonify
from Modules.DockerModule import DockerModule
import json

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/docker_ger/")
def dexter_ger():
	list = DockerModule()
	container = list.listContainers()
	return render_template("docker_ger.html",containers=container)


if __name__ == '__main__':
	app.run(debug=True)