# -*- coding: utf-8 -*-


dni = open("dni.txt","rt",encoding='utf8')
datos_dni = dni.read()

#todos los elementos de la cadena datos_noticia lo pasmos a lista
lista = datos_dni.split()
#listaconcriterio = datos_noticia.split('el')

print(f'Original: {datos_dni}')
print(lista)
print(lista[0])
print(lista[1])
#print(listaconcriterio)

fecha_nacimiento = open("fecha_nacimiento.txt","rt",encoding='utf8')
datos_fecha_nacimiento = fecha_nacimiento.read()

#todos los elementos de la cadena datos_noticia lo pasmos a lista
lista = datos_fecha_nacimiento.split()
#listaconcriterio = datos_noticia.split('el')

print(f'Original: {datos_fecha_nacimiento}')
print(lista)
print(lista[0])
print(lista[1])
#print(listaconcriterio)

nombres = open("nombres.txt","rt",encoding='utf8')
datos_nombres = nombres.read()

#todos los elementos de la cadena datos_noticia lo pasmos a lista
lista = datos_nombres.split()
#listaconcriterio = datos_noticia.split('el')

print(f'Original: {datos_nombres}')
print(lista)
print(lista[0])
print(lista[1])
#print(listaconcriterio)