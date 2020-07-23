# -*- coding: utf-8 -*-


noticia = open("dni.txt","rt",encoding='utf8')
datos_dni = dni.read()

#todos los elementos de la cadena datos_noticia lo pasmos a lista
lista = datos_dni.split()
#listaconcriterio = datos_noticia.split('el')

print(f'Original: {datos_dni}')
print(lista)
print(lista[0])
print(lista[1])
#print(listaconcriterio)