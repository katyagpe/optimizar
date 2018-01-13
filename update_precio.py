# -*- coding: utf-8 -*-

#********************************************************#
# Modificación de productos.                             #
#********************************************************#
import os
import csv
import xmlrpclib
import re

HOST='localhost'
PORT=8069
DB='4toangulo_pruebas'
USER='salas-rodriguez@hotmail.com'
PASS='agosto1993'
url ='http://%s:%d/xmlrpc/' % (HOST,PORT)

common_proxy = xmlrpclib.ServerProxy(url+'common')
object_proxy = xmlrpclib.ServerProxy(url+'object')
uid = common_proxy.login(DB,USER,PASS)


print "Entraste como  %s (uid:%d)" % (USER,uid)

def _update_mass(estado):
    if estado is True:
        path_file = './update.csv'
        archive = csv.DictReader(open(path_file))
        cont = 1


        for field in archive:


            productos = {
                'default_code':field['default_code'],
                'list_price':field['list_price'],
            }

            
            product = object_proxy.execute(DB,uid,PASS,'product.template','search',[('default_code','=',field['default_code'])])

            for default_code in product:
                do_write = object_proxy.execute(DB,uid,PASS,'product.template', 'write',default_code, {'list_price':field['list_price']})
                
                if do_write:
                    print "Referencia interna:",field['default_code']
                cont = cont + 1

def __main__():
    print 'Ha comenzado el proceso'
    _update_mass(True)
    print 'Ha finalizado la carga tabla'
__main__()