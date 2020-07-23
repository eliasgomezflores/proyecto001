# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:56:11 2020

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


def menuDatos():
    print("\n---- Datos Persona ----")
    print("1. Listar")
    print("2. Agregar")
    print("3. Eliminar")
    print("4. Modificar")
    print("5. Salir")
             
def listar():
    dnitxt = open("dni.txt","rt", encoding='utf8')
    datos_dni=dnitxt.read()
    listadniconcriterio = datos_dni.split('\n')
        
    fecha_nacimientotxt = open("fecha_nacimiento.txt","rt", encoding='utf8')
    datos_fecha_nacimiento=fecha_nacimientotxt.read()
    listafecha_nacimientoconcriterio = datos_fecha_nacimiento.split('\n')
        
    nombrestxt = open("nombres.txt","rt", encoding='utf8')
    datos_nombres=nombrestxt.read()
    listanombresconcriterio = datos_nombres.split('\n')
        
    print("\n-- Listar Datos --")
    contador=0
    for contar in listanombresconcriterio:
        print(f"{listanombresconcriterio[contador]} || {listadniconcriterio[contador]} || {listafecha_nacimientoconcriterio[contador]}")
        contador+=1
    
    dnitxt.close() 
    fecha_nacimientotxt.close()
    nombrestxt.close() 
    
def eliminar():
    print("\n-- Eliminar Datos --")
    eliminardni=""
    eliminardni = input("Ingrese el DNi de la persona a eliminar: ")
    dnitxt = open("dni.txt","rt", encoding='utf8')
    datos_dni=dnitxt.read()
    listadniconcriterio = datos_dni.split('\n')
    
    fecha_nacimientotxt = open("fecha_nacimiento.txt","rt", encoding='utf8')
    datos_fecha_nacimiento=fecha_nacimientotxt.read()
    listafecha_nacimientoconcriterio = datos_fecha_nacimiento.split('\n')
        
    nombrestxt = open("nombres.txt","rt", encoding='utf8')
    datos_nombres=nombrestxt.read()
    listanombresconcriterio = datos_nombres.split('\n')
    
    contador=0
    existe=0
    for verificar in listadniconcriterio:
            if eliminardni == listadniconcriterio[contador]:
                existe=1
                eliminarnombre=listanombresconcriterio[contador]
                eliminarfecha=listafecha_nacimientoconcriterio[contador]
            contador+=1
                
    dnitxt.close() 
    
    if existe == 1:
        dni = open("dni.txt","r")
        fecha = open("fecha_nacimiento.txt","r")
        nombres = open("nombres.txt","r")
        lineasdni = dni.readlines()
        lineasfecha = fecha.readlines()
        lineasnombres = nombres.readlines()
        dni.close() 
        fecha.close()
        nombres.close()
        
        dni = open("dni.txt","w")
        fecha = open("fecha_nacimiento.txt","w")
        nombres = open("nombres.txt","w")
        
        for contar in lineasdni:
             if contar!=eliminardni+"\n":
                 dni.write(contar)
                
        dni.close()
        
        for contar in lineasfecha:
             if contar!=eliminarfecha+"\n":
                 fecha.write(contar)
                
        fecha.close()
        
        for contar in lineasnombres:
             if contar!=eliminarnombre+"\n":
                 nombres.write(contar)
                
        nombres.close()
        
        print(f"\nLos datos de {eliminarnombre} han sido eliminados exitosamente")
        
    else:
        print("\nLa persona no existe")
        
    
def agregar():
    print("\n-- Agregar datos --")
    nombre = input("Nombre Completo: ")
    dni = input("DNI: ")
    fecha = input("Fecha(xx/xx/xxxx): ")
    
    dnitxt = open("dni.txt","at", encoding='utf8')
    dnitxt.write("\n" + dni)
    dnitxt.close() 
    
    fecha_nacimientotxt = open("fecha_nacimiento.txt","at", encoding='utf8')
    fecha_nacimientotxt.write("\n"+ fecha)
    fecha_nacimientotxt.close() 
    
    nombrestxt = open("nombres.txt","at", encoding='utf8')
    nombrestxt.write("\n" + nombre)
    nombrestxt.close() 

    
def modificar():
    print("\n-- Modificar Datos --")
    modificardni=""
    modificardni = input("Ingrese el DNi de la persona a modificar: ")
    dnitxt = open("dni.txt","rt", encoding='utf8')
    datos_dni=dnitxt.read()
    listadniconcriterio = datos_dni.split('\n')
    
    fecha_nacimientotxt = open("fecha_nacimiento.txt","rt", encoding='utf8')
    datos_fecha_nacimiento=fecha_nacimientotxt.read()
    listafecha_nacimientoconcriterio = datos_fecha_nacimiento.split('\n')
        
    nombrestxt = open("nombres.txt","rt", encoding='utf8')
    datos_nombres=nombrestxt.read()
    listanombresconcriterio = datos_nombres.split('\n')
    
    contador=0
    existe=0
    for verificar in listadniconcriterio:
            if modificardni == listadniconcriterio[contador]:
                existe=1
                modificarnombre=listanombresconcriterio[contador]
                modificarfecha=listafecha_nacimientoconcriterio[contador]
            contador+=1
                
    dnitxt.close() 
    
    if existe == 1:
        dni = open("dni.txt","r")
        fecha = open("fecha_nacimiento.txt","r")
        nombres = open("nombres.txt","r")
        lineasdni = dni.readlines()
        lineasfecha = fecha.readlines()
        lineasnombres = nombres.readlines()
        dni.close() 
        fecha.close()
        nombres.close()
        
        dni = open("dni.txt","w")
        fecha = open("fecha_nacimiento.txt","w")
        nombres = open("nombres.txt","w")
        
        print(f"\nModificando datos de {modificarnombre}\n")
        
        
        for contar in lineasdni:
             if contar!=modificardni+"\n":
                 dni.write(contar)
             else:
                 dni.write(input("Nuevo Dni: ")+"\n")
                
        dni.close()
        
        for contar in lineasfecha:
             if contar!=modificarfecha+"\n":
                 fecha.write(contar)
             else:
                 fecha.write(input("Nueva Fecha(xx/xx/xxxx): ")+"\n")
                
        fecha.close()
        
        for contar in lineasnombres:
             if contar!=modificarnombre+"\n":
                 nombres.write(contar)
             else:
                 nombres.write(input("Nuevo Nombre: ")+"\n")
                
        nombres.close()
        
        print("\nLos datos han sido modificados exitosamente")
        
    else:
        print("\nLa persona no existe")
    
def salir():
    print("\nGracias por visitar")

def menu():
    print("\n--------- MENU ---------")
    print("1. Iniciar Sesion")
    print("2. Registrarse")
    
def agregarUsuario():
    existeusuario=1
    while existeusuario==1:
        existeusuario=0
        contador=0
        print("\n------ REGISTRARSE ------")
        usuario = input("Usuario: ")
        clave = input("Clave: ")
    
        usuariotxt = open("usuario.txt","rt", encoding='utf8')
        datos_usuario=usuariotxt.read()
        listausuarioconcriterio = datos_usuario.split('\n')
        
        for verificar in listausuarioconcriterio:
            if usuario == listausuarioconcriterio[contador]:
                existeusuario=1
            contador+=1
                
        usuariotxt.close()
    
        if existeusuario!=1:
            usuariotxt = open("usuario.txt","at", encoding='utf8')
            usuariotxt.write("\n" + usuario)
            usuariotxt.close() 
    
            clavetxt = open("clave.txt","at", encoding='utf8')
            clavetxt.write("\n" + clave)
            clavetxt.close() 
            
            print("\nEl usuario fue creado exitosamente")
        
        else:
            print("\nEl usuario ya existe, vuelva a intentar")
    

while True:
    opcionmenu=0
    
    try:
        menu()
        opcion=int(input("-->Opcion: "))

    except:
        print("Opcion Invalida")

    #cuando no detecta error
    else:
        if opcion==1: 
            print("\n---- INICIAR SESION ----")
            usuario=input("Usuario: ")
            clave=input("Clave: ")
            
            usuariotxt = open("usuario.txt","rt", encoding='utf8')
            datos_usuario=usuariotxt.read()
            listausuarioconcriterio = datos_usuario.split('\n')
        
            clavetxt = open("clave.txt","rt", encoding='utf8')
            datos_clave=clavetxt.read()
            listaclaveconcriterio = datos_clave.split('\n')
            menudatos=0
            contador=0
            for verificar in listausuarioconcriterio:
                if usuario == listausuarioconcriterio[contador] and clave == listaclaveconcriterio[contador]:
                    menudatos=1
                contador+=1
            
            usuariotxt.close()
            clavetxt.close()
            
            if menudatos == 1:
                while opcionmenu != 5:
                    menuDatos();
                    opcionmenu=int(input("-->Opcion: "))
                    
            
                    if opcionmenu==1:
                        listar()
                    
                    elif opcionmenu == 2:
                        agregar()
                        
                    elif opcionmenu == 3:
                        eliminar()
                            
                    elif opcionmenu == 4:
                        modificar()
                                
                    elif opcionmenu == 5:
                        salir()
                
                    else:
                        print("\nOpcion Invalida")
                
            else:
                print("\nUsuario o Clave Incorrecto")
        
        elif opcion==2:
            agregarUsuario()

        else:
            print("\nFuera de Rango")

    if opcionmenu==5:
        break
    
    
 