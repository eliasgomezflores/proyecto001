# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:33:21 2020

@author: Administrador
"""


import sqlite3

def menuDatos():
    print("\n---------- MENU ----------")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Modificar")
    print("4. Listar")
    print("5. Salir")
    
def salir():
    print("\nGracias por visitar")
    
def crearBD(nombre):
    nombre=nombre+".db"
    conexion = sqlite3.connect(nombre)
    
    tabla_producto = """CREATE TABLE producto(
                     idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                     nombre TEXT,
                     precio REAL,
                     f_vencimiento TEXT,
                     stock INTEGER,
                     marca TEXT,
                     estado TEXT
                )
            """
    cursor = conexion.cursor()
    cursor.execute(tabla_producto)
    cursor.close()
    conexion.close()

def modificar(nombre, mod, newm, idp):
    conexion = sqlite3.connect(nombre+'.db')
    cursor = conexion.cursor()
    
    consulta = f"""UPDATE producto
                  SET {mod} = '{newm}'
                  WHERE IDPRODUCTO = {idp};
    """
    
    cursor.execute(consulta)
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar(nombre, idp):
    conexion = sqlite3.connect(nombre+'.db')
    cursor = conexion.cursor()
    
    consulta = f"""DELETE FROM producto
                  WHERE idproducto = {idp}
                  
    """
    cursor.execute(consulta)
    conexion.commit()
    cursor.close()
    conexion.close()

def listar(nombre):   
    conexion = sqlite3.connect(nombre+'.db')
    cursor = conexion.cursor()
    consulta = """SELECT * FROM producto
                   WHERE precio > 1
                   ORDER BY nombre
            """
    cursor.execute(consulta)
    productos = cursor.fetchall()

    for prod in productos:
        print(prod)
        
    cursor.close()
    conexion.close()

def agregar(nombre, n, p, f, s, m, e):
    conexion = sqlite3.connect(nombre+'.db')
      
    consulta = f"""INSERT INTO 
    producto(NOMBRE, PRECIO, F_VENCIMIENTO, STOCK, MARCA, ESTADO)
    VALUES('{n}', '{p}', '{f}', '{s}', '{m}', '{e}')
    """
    conexion.cursor()
    conexion.execute(consulta)
    conexion.commit()

    conexion.close()

opcionmenu=0
while opcionmenu != 2:
    print("\n----- MENU PRINCIPAL -----")
    print("1. Construir Base de Datos")
    print("2. Salir")    
    opcionmenu=int(input("-->Opcion: "))

    if opcionmenu==1:
        nombre = input("Nombre de la BD: ")
        crearBD(nombre)
                    
    elif opcionmenu == 2:
        salir()
                
    else:
        print("\nOpcion Invalida")



while opcionmenu != 5:
    menuDatos();
    opcionmenu=int(input("-->Opcion: "))
                    
    if opcionmenu == 1:
        nombre = input("Base de datos: ")
        n = input("Nombre:  ")
        p = input("Precio: ")
        f = input("Fecha de vencimiento: ")
        s= input("Stock: ")
        m = input("Marca: ")
        e = input("Estado (A o I): ")
        agregar(nombre, n, p, f, s, m, e)
                        
    elif opcionmenu == 2:
        nombre = input("Base de datos: ")
        listar(nombre)
        idp = input("Ingresar el id del producto que desea eliminar: ")
        eliminar(nombre, idp)
                            
    elif opcionmenu == 3:
        nombre = input("Base de datos: ")
        listar(nombre)
        mod = input("Campo que desea modificar: ")
        newm = input("Ingrese el nuevo valor: ")
        idp = input("Ingrese la id que desea modificar: ")
        modificar(nombre, mod, newm, idp)
                          
    elif opcionmenu == 4:
        nombre = input("Base de datos: ")
        listar(nombre)
                        
    elif opcionmenu == 5:
        salir()
                
    else:
        print("\nOpcion Invalida")