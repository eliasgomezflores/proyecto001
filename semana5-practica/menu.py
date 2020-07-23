
# -*- coding: utf-8 -*-
















import os
import gestionar_archivos

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Listar")
    print("2. Agregar")
    print("3. Eliminar")
    print("4. Modificar")
    print("5. Salir.")
    
def listar():
    print("-- Listar Nombres --")
    archivo1 = 'dni.txt'
    archivo2 = 'fecha_nacimiento.txt'
    archivo3 = 'nombres.txt'
    print('DNI:')
    print(gestionar_archivos.leer_archivo(archivo1))
    print('\nFECHAS DE NACIMIENTO:')
    print(gestionar_archivos.leer_archivo(archivo2))
    print('\nNOMBRES:')
    print(gestionar_archivos.leer_archivo(archivo3))
       
 
def agregar():
    print("-- Agregar persona a una lista --")
    archivo = 'dni.txt'
    contenido = input("DNI: ")
    gestionar_archivos.agregar_contenido_archivo(archivo,contenido)
    archivo = 'fecha_nacimiento.txt'
    contenido = input("Fecha de nacimiento: ")
    gestionar_archivos.agregar_contenido_archivo(archivo,contenido)
    archivo = 'nombres.txt'
    contenido = input("Nombres: ")
    gestionar_archivos.agregar_contenido_archivo(archivo,contenido)
    
    
#def eliminar():
 #   print("--Eliminar Persona --")
 #   archivo = input("Archivo: ")
 #   gestionar_archivos.eliminar_archivo(archivo)
    
#def listar():
 #   print("-- Crea Archivo --")
 #   archivo = input("Archivo: ")
 #   contenido = input("contenido: ")
 #   gestion_archivos.crear_archivo(archivo,contenido)
   
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
		listar()
        
	elif opcionMenu=="2":
		agregar()
    
	elif opcionMenu=="3":
		agregar()
        
	elif opcionMenu=="4":
		listar()
        
	elif opcionMenu=="5":
		salir()
	else:
		error()
        
    
    
