# -*- coding: utf-8 -*-
import camelcase
nombre = "gomez flores elias"
print(nombre.upper())
print(nombre.title())

#que pasaria si ahora el problema pidiera que el
#nombre de elias y gomez no se muestre en formato titulo

cam = camelcase.CamelCase()
print("mostramos ahora con macelcase")

cam2 = camelcase.CamelCase('elias','gomez')
print(cam2.hump(nombre))