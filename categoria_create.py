# -*- coding: utf-8 -*-
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


def _create(estado):
    if estado is True:
        path_file = './categoria.csv'
        archive = csv.DictReader(open(path_file))
        cont = 1

        for field in archive:

            productos = {
                'id':field['id'],
                'name':field['name'],
            }

            do_write = object_proxy.execute(DB, uid, PASS, 'product.category','create',productos)
            if do_write:
                print "OK",cont
            cont = cont + 1
            print "Contador:",cont

def __main__():
    print 'Ha comenzado el proceso'
    _create(True)
    print 'Ha finalizado la carga tabla'
__main__()