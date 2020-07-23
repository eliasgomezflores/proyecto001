# -*- coding: utf-8 -*-
#vamos a suponer una operacion sencillla

#vamos a gestionar los errores, con try
try:
    numerador = float(input('Numerador: '))
    denominador = float(input('Denominador: '))
    resultado = numerador / denominador
    print(f'Resultdado: {resultado}')

#tambien puedo categorizar mis excepciones
except ZeroDivisionError:
    print('No es posible dividir entre CERO')
    
#except se ejecuta solo cuando se detecte un error dentro del try
#si no se detecta los errores en las categorias definidas
#se ejecuta este except
except:
    print('Hubo un error')

#cuado no se detecte errores
else:
    print('La division se realizo con exito')

#exista o no error siempre se ejecutara al final el finally
finally:
    print('La operacion TERMINO...')







