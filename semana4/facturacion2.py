# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:14:36 2020

@author: Hp
"""


import financieros

total = 1000.49
print(f"Subtotal: {financieros.obtenersubtotalcontotal(total): .2f}")
print(f"IGV: {financieros.obtenerigvcontotal(total): .2f}")
print(f"Total: {total}")
