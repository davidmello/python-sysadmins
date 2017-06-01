#!/usr/bin/python

import yaml

class DexterbookParser:

    def __init__(self,book):
        try:
            with open(book,'r') as f:
                self.book = yaml.load(f.read())

        except Exception as e:
            print "Falhou ao converter o dexterbook: ",e


    def get(self):
        return self.book

