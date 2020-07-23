# -- coding: utf-8 --
"""
Created on Thu Jun 25 13:35:56 2020

@author: USUARIO
"""
import sqlite3

def crearBD():
    conexion = sqlite3.connect("ventas.db")
    
    tabla_producto = """CREATE TABLE IF NOT EXISTS producto(
                     idproducto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                     nombre TEXT,
                     precio REAL,
                     codigo TEXT UNIQUE,
                     estado TEXT DEFAULT 'A'
                )
            """
    cursor = conexion.cursor()
    cursor.execute(tabla_producto)
    cursor.close()
    conexion.close()
    
    conexion = sqlite3.connect("ventas.db")
    tabla_usuario = """CREATE TABLE IF NOT EXISTS usuario(
                     idusuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                     usuario TEXT UNIQUE,
                     clave TEXT
                )
            """
    cursor = conexion.cursor()
    cursor.execute(tabla_usuario)
    cursor.close()
    conexion.close()
    
    usuariotxt = open("usuarios.txt","rt", encoding='utf8')
    datos_usuario=usuariotxt.read()
    listausuarioconcriterio = datos_usuario.split('\n')
        
    clavetxt = open("claves.txt","rt", encoding='utf8')
    datos_clave=clavetxt.read()
    listaclaveconcriterio = datos_clave.split('\n')

    nombretxt = open("nombre.txt","rt", encoding='utf8')
    datos_nombre=nombretxt.read()
    listanombreconcriterio = datos_nombre.split('\n')
 
    preciotxt = open("precio.txt","rt", encoding='utf8')
    datos_precio=preciotxt.read()
    listaprecioconcriterio = datos_precio.split('\n')
 
    codigotxt = open("codigo.txt","rt", encoding='utf8')
    datos_codigo=codigotxt.read()
    listacodigoconcriterio = datos_codigo.split('\n')
     
    conexion=sqlite3.connect("ventas.db")
    cursor=conexion.cursor()
    
    for u, c in zip(listausuarioconcriterio, listaclaveconcriterio):
        consulta_tablausuario=f"""INSERT INTO 
                    USUARIO(USUARIO,CLAVE) 
                    VALUES ('{u}',{c})
                    """
        cursor.execute(consulta_tablausuario)

    for n, p ,x in zip(listanombreconcriterio, listaprecioconcriterio, listacodigoconcriterio):
        consulta_tablaproducto=f"""INSERT INTO 
                    PRODUCTO(NOMBRE,PRECIO,CODIGO) 
                    VALUES ('{n}',{p},'{x}')
                    """
        cursor.execute(consulta_tablaproducto)
         
        
        
    conexion.commit()   
    usuariotxt.close() 
    clavetxt.close()
    nombretxt.close()
    preciotxt.close()
    codigotxt.close()
 
    

crearBD()



def menuprincipal():
    print("\n--------- MENU ---------")
    print("1. Iniciar Sesion")
    print("2. Registrarse")
    print("3. Salir")
    
def salir1():
    print("\nGracias por visitar")

def agregarUsuario(u1, c1):
    conexion = sqlite3.connect('ventas.db')
    cursor = conexion.cursor()
      
    consulta = f"""INSERT INTO 
    usuario(USUARIO, CLAVE)
    VALUES('{u1}', '{c1}')
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
    precio=float(input("ingrese precio: "))
    codigo=input("Ingrese codigo del producto: ") 
    

    lista_productos=[(nombre,precio,codigo)]

    consulta_producto="""INSERT INTO 
                PRODUCTO(NOMBRE,PRECIO,CODIGO) 
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
                         where codigo = '{cod}' '''
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
        listar()
        eliminar()

    elif opcion == 4:
        listar()
        modificar()
        
    elif opcion == 5:
        salir1()
        
    else:
        print("\nOpcion Invalida")



