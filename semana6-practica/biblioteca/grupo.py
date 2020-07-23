# -- coding: utf-8 --
"""
Created on Thu Jun 11 16:44:55 2020

@author: NATHAN
"""

####################
#INTEGRANTES
#- NATHAN SILVERA IÑIGO
#- JOSE ORLANDO RAMOS
#- OSCAR VILCA RIVERA
#- JEAN CARLOS CRUZ HUANCA
#- ELIAS GOMEZ FLORES
####################


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

def eliminar(ID):
    import sqlite3
    conexion = sqlite3.connect('producto.bd')
    cursor = conexion.cursor()
    consulta = """ DELETE FROM PRODUCTO
                WHERE
                    idproducto = ID
            """
    cursor = conexion.cursor()
    cursor.execute(consulta)
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
        agregar()
                        
    elif opcionmenu == 2:
        ID=int(input("ingrese el ID del producto"));
        eliminar()
                            
    elif opcionmenu == 3:
        modificar()
                          
    elif opcionmenu == 4:
        listar()
                        
    elif opcionmenu == 5:
        salir()
                
    else:
        print("\nOpcion Invalida")