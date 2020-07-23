# -- coding: utf-8 --
"""
 Created on Thu May 28 16:46:14 2020

 @author: Administrador
"""
import gestion_de_archivos1
import filecmp


usuario=input("Ingrese usuario: ")
clave=input("Ingrese clave: ") 


usuariotxt = open("usuario.txt","rt", encoding='utf8')
datos_usuario=usuariotxt.read()
listausuarioconcriterio = datos_usuario.split('\n')
        
clavetxt = open("clave.txt","rt", encoding='utf8')
datos_clave=clavetxt.read()
listaclaveconcriterio = datos_clave.split('\n')
        
for verificar in listausuarioconcriterio:
    
        
 if usuario == listausuarioconcriterio[0] and clave == listaclaveconcriterio[0]:
    
    print("Datos correctos ingresados, Bienvenido administrador")



    def menu():
        print("*MENU PRINCIPAL*")
        print("1. crear archivo")
        print("2. eliminar archivo")
        print("3. agregar contenido al archivo")
        print("4. Mostrar contenido del archivo")
        print("5.Salir del Menu")
    

    
    def crear():
        print("Crear nombre de archivo")
        archivo=input("Archivo: ")
        print("agregar contenido al archivo")
        contenido=input("Contenido: ")
        gestion_de_archivos1.crear_archivo(archivo,contenido)
    
    def eliminar():
        print("eliminar archivo")
        archivo=input("archivo: ")
        gestion_de_archivos1.eliminar_archivo(archivo)
    
    def agregar():
        print("agregar datos")
        archivo=input("Archivo: ")
        nombre2=input("Nombre completo: ")
        dni2=input("DNI: ")
        fecha2=input("Fecha: ")
    
        gestion_de_archivos1.agregar_contenido_archivo(archivo,nombre2,dni2,fecha2)
    
    def mostrar():
        print("Mostrar contenido de un archivo")
        archivo=input("archivo: ")
        print(gestion_de_archivos1.leer_archivo(archivo))
    
    def salir_del_menu():
        print("Ha salido del menu principal")

    def error(): 
        print("opcion no valida ,elija otra vez")

    
    opcion=1
   
    while opcion != 5:
       
        menu()
        opcion=int(input("seleccione opcion: "))
        if opcion==1:
         crear()
        elif opcion==2:
         eliminar()
        elif opcion==3:
         agregar()
        elif opcion==4:
         mostrar()
        elif opcion==5:
         salir_del_menu()
        else:
          error()   
         
else:
    print("Datos incorrectos, vuelva a registrarse")