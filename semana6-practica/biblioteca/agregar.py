# -*- coding: utf-8 -*-

import sqlite3
a=1;

if a == 1:
    s_nombre=input('ingrese nombre: ')
    s_precio=input('ingrese precio: ')
    s_f_vencimiento=input('ingrese f_vencimiento: ')
    s_stok=input('ingrese stock: ')
    s_marca=input('ingrese marca: ')
    
    
    
    
conexion = sqlite3.connect('practica06.db')

#Recordemos al insertar que el id es automaticamente



consulta = """ INSERT INTO
                PRODUCTO(NOMBRE,PRECIO,F_VENCIMIENTO,STOCK,MARCA,ESTADO)
                VALUES('s_nombre','s_precio','s_f_vencimiento','s_stock','s_marca','A')
            """
cursor = conexion.cursor()
cursor.execute(consulta)

conexion.commit()



conexion.close()

















