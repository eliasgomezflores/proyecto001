# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

igv = 0.18

def obtenerigvconsubtotal(subtotal):
    return subtotal*igv
    
def obtenertotalconsubtotal(subtotal):
    return subtotal*(1+igv)

def obtenersubtotalcontotal(total):
    return total/(1+igv)

def obtenerigvcontotal(total):
    return total - obtenersubtotalcontotal(total)


