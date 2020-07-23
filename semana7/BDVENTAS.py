# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:22:21 2020

@author: USUARIO
"""

import sqlite3


def menuprincipal():
    print("\n--------- MENU ---------")
    print("1. Iniciar Sesion")
    print("2. Registrarse")
    print("3. Salir")
    
def salir1():
    print("\nGracias por visitar")

def agregarUsuario(u, c):
    conexion = sqlite3.connect('ventas.db')
    cursor = conexion.cursor()
      
    consulta = f"""INSERT INTO 
    seguridad(USUARIO, CLAVE)
    VALUES('{u}', '{c}')
    """
    conexion.cursor()
    conexion.execute(consulta)
    conexion.commit()

    cursor.close()
    conexion.close()
    
def agregar():
    conexion=sqlite3.connect("ventas.db")
    cursor=conexion.cursor()
    

    nombre=input("ingrese nombre del producto: ")
    codigo=input("Ingrese codigo del producto: ")   
    precio=float(input("ingrese precio: "))
    estado=input("Ingrese estado: ")
    

    lista_productos=[(nombre,codigo,precio,estado)]

    consulta_producto="""INSERT INTO 
                PRODUCTO(NOMBRE,CODIGO,PRECIO,ESTADO) 
                VALUES (?,?,?,?,)
            """
    
    cursor.executemany(consulta_producto,lista_productos)
    conexion.commit()
    cursor.close()
    conexion.close()
    
    
def modificar():
    print ('Modificar empleado...')
    idproducto = input('Indique el id del empleado a modificar: ')
    nombre = input("Nombre: ")
    codigo = input("Codigo: ")  
    precio = input("Precio: ")
    estado = input("Estado: ")
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    consulta_modif = f'update producto set nombre = "{nombre}",codigo="{codigo}",precio = "{precio}",estado = "{estado}" where idproducto = "{idproducto}"'
    cursor = conexion.cursor()
    cursor.execute (consulta_modif)
    conexion.commit()
    conexion.close()
    print('Producto modificado')
    
def listar():
    print('Listar productos')
    conexion = sqlite3.connect("ventas.db")

    consulta = """ SELECT * 
                    FROM producto 
                """
    cursor = conexion.cursor()
    cursor.execute(consulta)
    
    producto = cursor.fetchall()
    print('idproducto \t nombre \t codigo \t precio\t estado')
    for producto in producto:
        print(f'\t{producto[0]}\t {producto[1]}\t {producto[2]}\t {producto[3]}\t {producto[4]}')
    
    conexion.close()

def eliminar():
    conexion = sqlite3.connect('ventas.db')
    cursor = conexion.cursor()
    
    idp = int(input("Ingresar el id del producto que desea eliminar: "))
        
    consulta = f"""DELETE FROM producto
                  WHERE idproducto = {idp}
                  
                  """
    cursor.execute(consulta)
    conexion.commit()
    cursor.close()
    conexion.close()
def salir():
    print("Salida con exito")
def error():
    print("escriba una opcion valida...")    

def menu():
    print('\n*Menu*')
    print('1. Listar')
    print('2. Agregar')
    print('3. Eliminar')
    print('4. Modificar')
    print('5. Salir')
    

opcionmenu=0
probar=0
while opcionmenu != 3:
    menuprincipal();    
    opcionmenu=int(input("-->Opcion: "))

    if opcionmenu==1:
        print("\n--- Iniciar Sesion ---")
        u = input("Usuario:  ")
        c = input("Clave: ")
        contador=0
        conexion = sqlite3.connect('ventas.db')
        cursor = conexion.cursor()
      
        consulta = """SELECT *
                    FROM usuario
            """
        cursor.execute(consulta)
        productos = cursor.fetchall()

        for prod in productos:
            if prod[1]==u and prod[2]==c:
                contador+=1
            
        if contador==0:
            print("\nUsuario o Clave Incorrecto")
        
        if contador==1:
            print(f"\nBienvenido Al sistema {u}")
            opcionmenu=3
            probar=1
    
        cursor.close()
        conexion.close()
        
    
    elif opcionmenu==2:
        print("\n--- Registrarse ---")
        u = input("Usuario:  ")
        c = input("Clave: ")
        agregarUsuario(u,c)
                
    elif opcionmenu == 3:
        salir()
                
    else:
        print("\nOpcion Invalida")
        
if probar==0: 
    if opcionmenu == 3:
        opcion=5
else:
    opcion=0
    
while opcion != 5:
    menu()
    opcion=int(input("-->Opcion: "))
    if opcion == 1:
        listar()
    
    elif opcion == 2:
        agregar()
        
    elif opcion == 3:
        eliminar()

    elif opcion == 4:
        modificar()
        
    elif opcion == 5:
        salir1()
        
    else:
        print("\nOpcion Invalida")



