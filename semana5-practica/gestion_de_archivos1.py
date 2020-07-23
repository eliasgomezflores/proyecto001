# -- coding: utf-8 --
"""
Created on Thu Jun  4 16:10:15 2020

@author: Administrador
"""


import os

def crear_archivo(nombre,contenido):
    archivo=open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()
    
def eliminar_archivo(nombre):
   os.remove(nombre)
    
def agregar_contenido_archivo(nombre,nombre2,dni2,fecha2):
      archivo=open(nombre,"at")
      archivo.write("\n"+nombre2+"\n"+dni2+"\n"+fecha2)
      archivo.close()
      
def leer_archivo(nombre):
     archivo=open(nombre,"rt",encoding="utf8")
     contenido=archivo.read()
     return contenido