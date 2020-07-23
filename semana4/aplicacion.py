# -*- coding: utf-8 -*-
import os
import gestion_archivos

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Crear Archivo.")
    print("2. Eliminar Archivo.")
    print("3. Agregar Contenido.")
    print("4. Mostrar contenido del archivo.")
    print("5. Salir.")
    
    
def crear():
    print("-- Crea Archivo --")
    archivo = input("Archivo: ")
    contenido = input("contenido: ")
    gestion_archivos.crear_archivo(archivo,contenido)
    
def eliminar():
    print("--Eliminar Archivo --")
    archivo = input("Archivo: ")
    gestion_archivos.eliminar_archivo(archivo)
    
def agregar():
    print("-- Agregar datos a un archivo --")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_archivos.agregar_contenido_archivo(archivo,contenido)

def listar():
    print("-- Mostrar contenido de un archivo --")
    archivo = input("Archivo: ")
    print(gestion_archivos.leer_archivo(archivo))
    
def salir():
    print("adios")

def error():
    print ("")
    input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    
    
    
opcionMenu = 1   
    
while opcionMenu!=5:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = int(input("inserta una opcion >> "))
 
	if opcionMenu=="1":
		crear()
        
	elif opcionMenu=="2":
		eliminar()
    
	elif opcionMenu=="3":
		agregar()
        
	elif opcionMenu=="4":
		listar()
        
	elif opcionMenu=="5":
		salir()
	else:
		error()
        
    
    