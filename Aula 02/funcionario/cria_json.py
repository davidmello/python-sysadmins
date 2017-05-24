#!/usr/bin/python

import json


data = [
		{
		 "id":1, 
		 "nome":"David Mello", 
		 "dependentes":[{
		 			"id":1, 
		 			"nome":"Nina",
		 			"idade":"11"},
		 			{
		 			"id":2,
		 			"nome":"Serena",
		 			"idade":"13"
		 			}]
		},
		{
		 "id":2,
		 "nome":"David Hasson", 
		 "dependentes":[{
		 			"id":1, 
		 			"nome":"Nameless",
		 			"idade":"10"
		 			}]
		 }
		]
json_data = json.dumps(data)

print json_data