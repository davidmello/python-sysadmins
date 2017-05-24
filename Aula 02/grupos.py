#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,jsonify

grupos = Blueprint('grupos', __name__)

@grupos.route("/grupos")
def list_grupos():
	data = {"message":"Aqui serao listados os grupos cadastrados"}
	return jsonify(data)
