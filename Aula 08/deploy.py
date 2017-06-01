#!/usr/bin/python

from Module.DexterbookParser import DexterbookParser
import argparse


class DeployTool:
    def __init__(self):
        try:
            self.parser = argparse.ArgumentParser()
            self.parser.add_argument('-i',help="Essa opcao indica o caminho do DexterBook que ira realizar o deploy")
        except Exception as e:
            print "Falhou ao criar argumentos: ",e

    def getArgs(self):
        return self.parser.parse_args()



if __name__ == '__main__':
    dt = DeployTool()
    args = dt.getArgs()
    book = DexterbookParser(args.i)
    for i in book.get().get("deploy-sequence").get("commands"):
        print i





