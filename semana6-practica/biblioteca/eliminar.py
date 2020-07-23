# -*- coding: utf-8 -*-
a=0;
if a == 0:
    ELIMINAR=input('numero del trabajador a eliminar: ')
    b=1;
 
    
if b == 1:    
    import sqlite3
    conexion = sqlite3.connect("practica06.db")
    cursor = conexion.cursor()
    consulta = """ DELETE FROM TRABAJADOR
                    WHERE
                    IDTRABAJADOR = ELIMINAR
                """
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()






