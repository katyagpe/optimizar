#! /usr/bin/env python
# -*- coding: utf-8 -*-

#********************************************************#
# Creacion de productos, el csv no debe contener acentos.#
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

def _create(estado):
    if estado is True:
        path_file = './alta.csv'
        archive = csv.DictReader(open(path_file))
        cont = 1

        for field in archive:
            
            productos = {
                'id':field['id'],
                'name':field['name'],
                'default_code':field['default_code'],
                'categ_id':field['categ_id'],
                'list_price':field['list_price'],
                'standard_price':field['standard_price'],
                'type':field['type'],
                'active':True,
            }
            do_write = object_proxy.execute(DB,uid,PASS,'product.template','create',productos)
            if do_write:
                cont = cont + 1
                print "Producto: ",field['name'], "#producto",field['id']
            else:
                print "Error"

def __main__():
    print 'Ha comenzado el proceso'
    _create(True)
    print 'Ha finalizado la carga tabla'
__main__()