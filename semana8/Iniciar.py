# -- coding: utf-8 --
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
    
    
def menuDatos():
    print("\n---------- MENU PRODUCTO ----------")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Modificar")
    print("4. Listar")
    print("5. Salir")

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
    
    codigo=input("Ingrese codigo del producto: ")
    nombre=input("Ingrese nombre del producto: ")
    precio=float(input("Ingrese precio: "))

    lista_productos=[(codigo,nombre,precio)]

    consulta_producto="""INSERT INTO 
                PRODUCTO(CODIGO,NOMBRE,PRECIO) 
                VALUES (?,?,?)
            """
    
    cursor.executemany(consulta_producto,lista_productos)
    conexion.commit()
    cursor.close()
    conexion.close()
    
    
def modificar():
    print ('Modificar producto...')
    cod = input('Indique el codigo del producto a modificar: ')
    nom = input("Nombre: ")
    pre = input("Precio: ")
    es = input("Estado: ")
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    consulta_modif = f'''update producto
                         set 
                         nombre = "{nom}",                         
                         precio = "{pre}",
                         estado = "{es}"
                         where codigo = {cod} '''
    cursor.execute(consulta_modif)
    conexion.commit()
    conexion.close()
    print('\nProducto modificado')
    
def listar():
    conexion = sqlite3.connect('ventas.db')
    cursor = conexion.cursor()
    consulta = """SELECT * FROM producto"""
    cursor.execute(consulta)
    productos = cursor.fetchall()

    for prod in productos:
        print(prod)
    
    cursor.close()
    conexion.close()

def eliminar():
    conexion = sqlite3.connect('ventas.db')
    cursor = conexion.cursor()
    listar()
    cod = input("Ingresar el codigo del producto que desea eliminar: ")
    
    consulta = f"""DELETE FROM producto
                  WHERE codigo = '{cod}'
                  """
    cursor.execute(consulta)
    print("Producto eliminado.")
    conexion.commit()
    cursor.close()
    conexion.close()
    
def salir():
    print("Salida con exito")
def error():
    print("Escriba una opcion valida...")    

opcionmenu=0
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
        seguridad = cursor.fetchall()

        for seg in seguridad:
            if seg[1]==u and seg[2]==c:
                contador+=1
            
        if contador==0:
            print("\nUsuario o Clave Incorrecto")
        
        if contador==1:
            print(f"\nBienvenido Al sistema {u}")
            opcionmenu=3
    
        cursor.close()
        conexion.close()    
    
    elif opcionmenu==2:
        print("\n--- Registrarse ---")
        u = input("Usuario:  ")
        c = input("Clave: ")
        agregarUsuario(u,c)
                
    elif opcionmenu == 3:
        salir()
        opcionmenu=5
        break
                
    else:
        print("\nOpcion Invalida")
        
 
while opcionmenu!=5:
    menuDatos(); 
    opcionmenu=int(input("-->Opcion: "))
                    
    if opcionmenu == 1:
        agregar()
                        
    elif opcionmenu == 2:
        eliminar()
                            
    elif opcionmenu == 3:
        listar()
        modificar()
                          
    elif opcionmenu == 4:
        listar()
                        
    elif opcionmenu == 5:
        salir()
    else:
        error()