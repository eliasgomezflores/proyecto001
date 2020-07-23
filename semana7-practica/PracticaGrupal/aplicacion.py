# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:38:02 2020

@author: fabri
"""
import sqlite3

def contruir_base_datos():  
    conexion = sqlite3.connect("bdempleados.db")
    tabla_pais = """create table if not exists empleado(
                    idempleado INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    apellido TEXT,
                    edad INTEGER,
                    dni TEXT,
                    sueldo REAL
                    )
            """
    cursor = conexion.cursor()
    cursor.execute(tabla_pais)
    conexion.close()
    print('Base de datos construida')

def agregar():
    print('Agregar empleado:')
    
    nombre=input("Ingrese nombres:")
    apellidos=input("Ingrese apellidos:")
    edad=input("Ingrese edad: ")
    dni=input("Ingrese DNI: ")
    sueldo=input("Ingrese sueldo: ")
    conexion = sqlite3.connect("bdempleados.db")
    consulta = f'INSERT INTO empleado(nombre, apellido,edad,dni,sueldo) VALUES ("{nombre}","{apellidos}","{edad}","{dni}","{sueldo}")'
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()   

    conexion.close()

    print('Se agrego al empleado')
def eliminar():
    print('Eliminar empleado')
    dniE=input("Ingrese DNI: ")
    conexion = sqlite3.connect("bdempleados.db")
    cursor = conexion.cursor()
    consulta = """ DELETE FROM empleado
                    WHERE
                        dni = """+dniE+"""
                """
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()
def modificar():
    print ('Modificar empleado...')
    dni = input('Indique el dni del empleado a modificar: ')
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    sueldo = input("Sueldo: ")
    conexion = sqlite3.connect("bdempleados.db")
    cursor = conexion.cursor()
    consulta_modif = f'UPDATE EMPLEADO SET nombre="{nombre}",apellido = "{apellido}",edad = "{edad}",sueldo = "{sueldo}" where dni = "{dni}"'
    cursor = conexion.cursor()
    cursor.execute (consulta_modif)
    conexion.commit()
    conexion.close()
    print('empleado modificado')
def listar():
    print('Listar empleados')
    conexion = sqlite3.connect("bdempleados.db")

    consulta = """ SELECT * 
                    FROM empleado where sueldo>0  order by 2
                """
    cursor = conexion.cursor()
    cursor.execute(consulta)
    
    empleados = cursor.fetchall()
    print('id\t nombre\t apellido\t edad\t dni\t sueldo')
    for empleado in empleados:
        print(f'{empleado[0]}\t {empleado[1]}\t {empleado[2]}\t {empleado[3]}\t {empleado[4]} {empleado[5]}')
    
    conexion.close()
    
def salir():
    print("gracias...")
def error():
    print("escriba una opcion valida...")    

def menu():
    print('\n**Menu**')
    print('1. Construir base_datos')
    print('2. Agregar')
    print('3. Eliminar')
    print('4. Modificar')
    print('5. Listar')
    print('6. Salir')
    opcion = int(input('Ingrese una opcion: '))
    return opcion
   
while True:
    opcion = menu()
    switcher = {
        1: contruir_base_datos,
        2: agregar,
        3: eliminar,
        4: modificar,
        5: listar,
        6: salir
    }
    funcion = switcher.get(opcion)
    if funcion:
        if(funcion == salir):
            funcion()
            break
        funcion()
    else:
        error()