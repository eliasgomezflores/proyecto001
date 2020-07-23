# -*- coding: utf-8 -*-

import sqlite3

conexion = sqlite3.connect('bdbiblioteca.db')

#Recordemos al insertar que el id es automaticamente
consulta = """ INSERT INTO
                PAIS(NOMBRE,ESTADO)
                VALUES('Brasil','A')
            """
cursor = conexion.cursor()
cursor.execute(consulta)

conexion.commit()







conexion.close()



