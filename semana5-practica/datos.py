# -*- coding: utf-8 -*-
import csv
import os
def ingresar():
        archivo=open('usuario.txt',"rt",encoding="utf8")
        usuario=archivo.read()
    
        archivo1=open('clave.txt',"rt",encoding="utf8")
        clave=archivo1.read()
        
        a=input('Ingrese usuario: ')
        b=input('Ingrese clave: ')
        if a==usuario and clave==b:
            menu()
            
        else:
            print('Usuario o clave incorrecta')  
   



def listar():
    with open(r'C:\Users\Usuario\Desktop\nombres.txt',encoding="utf-8") as f:
        nombres = csv.reader(f, delimiter=',')
        print('Nombres')
        for fila in nombres:
            print(f"{fila[0]} ")
            
    with open(r'C:\Users\Usuario\Desktop\dni.txt',encoding="utf-8") as f:
        dni = csv.reader(f, delimiter=',')
        print('\nDNI')
        for fila in dni:
            print(f"{fila[0]} ")
             
    with open(r'C:\Users\Usuario\Desktop\fecha_nacimiento.txt',encoding="utf-8") as f:
        fecha = csv.reader(f, delimiter=',')
        print('\nFecha')
        for fila in fecha:
            print(f"{fila[0]} ")

def agregar():
    nombre=input('Ingrese nombre: ')
    dni=input('Ingrese DNI: ')
    fecha=input('Ingrese fecha: ')
    
    archivo = open('nombres.txt',"at")
    archivo.write(","+nombre)
    
    archivo1 = open('dni.txt',"at")
    archivo1.write("\n"+dni)
    
    archivo2 = open('fecha_nacimiento.txt',"at")
    archivo2.write("\n"+fecha)
    
def eliminar():
    dni=input('Ingrese DNI: ')
    f = open("dni.txt","r")
    lineas = f.readlines()
    f.close()
    
    f = open("dni.txt","w")
    for linea in lineas:
        if linea!=dni+"\n":
            f.write(linea)    
    f.close()
    
    
    nombre=input('Ingrese nombre: ')
    f1 = open("nombres.txt","r")
    lineas = f1.readlines()
    f1.close()
    f1 = open("nombres.txt","w")
    for linea in lineas:
        if linea!=nombre+"\n":
            f1.write(linea)    
    f1.close()
    
    
    fecha=input('Ingrese fecha: ')
    f2 = open("fecha.txt","r")
    lineas = f2.readlines()
    f2.close()
    f2 = open("fecha.txt","w")
    for linea in lineas:
        if linea!=fecha+"\n":
            f2.write(linea)    
    f2.close()
    
def modificar():
    print('No se puede modificar')


    
def menu():
    while True:
        
        print("\n********Menu*******")
        print("1.Listar ")
        print("2.Agregar")
        print("3.Eliminar")
        print("4.Modificar")
        print("5.Salir:")
        opcion=int(input("Digite una opcion: "))
        if opcion==1:
            listar()
        
        elif opcion==2:
            agregar()
           
        elif opcion==3:
            eliminar()

           
        elif opcion==4:
            modificar()
        
        elif opcion==5:
            break
    

ingresar()
    
    
    




