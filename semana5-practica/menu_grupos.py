# -- coding: utf-8 --
"""
Created on Thu Jun  4 15:56:11 2020

@author: USUARIO
"""


def menu():
    print("---- Datos Persona ----")
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
        
    print("-- Listar Datos --")
    for contar in listanombresconcriterio:
        print(f"{listanombresconcriterio[contar]} || {listadniconcriterio[contar]} || {listafecha_nacimientoconcriterio[contar]}")
    
    dnitxt.close() 
    fecha_nacimientotxt.close()
    nombrestxt.close() 
    
def eliminar():
    print("-- Eliminar Datos --")
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
    
    for verificar in listadniconcriterio:
            if eliminardni == listadniconcriterio[verificar] and clave == listaclaveconcriterio[verificar]:
                existe=1
                eliminarnombre=listanombresconcriterio[verificar]
                eliminarfecha=listafecha_nacimientoconcriterio[verificar]
        
                
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
                 fecha.write(contar)
                
        fecha.close()
        
    else:
        print("La persona no existe")
        
    
def agregar():
    print("-- Agregar datos --")
    nombre = input("Nombre Completo: ")
    dni = input("DNI: ")
    fecha = input("Fecha(xx/xx/xxxx): ")
    
    dnitxt = open("dni.txt","at", encoding='utf8')
    dnitxt.write(dni + "\n")
    dnitxt.close() 
    
    fecha_nacimientotxt = open("fecha_nacimiento.txt","at", encoding='utf8')
    fecha_nacimientotxt.write(fecha + "\n")
    fecha_nacimientotxt.close() 
    
    nombrestxt = open("nombres.txt","at", encoding='utf8')
    nombrestxt.write(nombre + "\n")
    nombrestxt.close() 

    
def modificar():
    print("-- Mostrar contenido de un archivo --")
    archivo = input("Archivo: ")
    noticia = open(archivo, "rt", encoding='utf8')
    datos_noticia = noticia.read()
    print(datos_noticia+"\n")
    
def salir():
    print("Gracias por visitar")


try:
    print("--------- MENU ---------")
    print("1. Iniciar Sesion")
    print("2. Registrarse")
    opcion=int(input("-->Opcion: "))

except:
    print("Opcion Invalida")

#cuando no detecta error
else:
    if opcion==1: 
        print("---- INICIAR SESION ----")
        usuario=input("Usuario: ")
        clave=input("Clave: ")
        
        usuariotxt = open("usuario.txt","rt", encoding='utf8')
        datos_usuario=usuariotxt.read()
        listausuarioconcriterio = datos_usuario.split('\n')
        
        clavetxt = open("clave.txt","rt", encoding='utf8')
        datos_clave=clavetxt.read()
        listaclaveconcriterio = datos_clave.split('\n')
        
        for verificar in listausuarioconcriterio:
            if usuario == listausuarioconcriterio[0] and clave == listaclaveconcriterio[0]:
                menudatos=1
                
        if menudatos == 1:
            menu();
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
                print("Opcion Invalida")
        else:
            print("Uuario o Clave Incorrecto")
        
    elif opcion==2:
        print("------ REGISTRARSE ------")
        usuario=input("Usuario: ")
        clave=input("Clave: ")

    else:
        print("Fuera de Rango")

finally:
    print("La operacion termino...")