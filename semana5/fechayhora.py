# -*- coding: utf-8 -*-

from datetime import datetime

fechayhora = datetime.now()

print(f'La fecha de hoy es: {fechayhora}')

#ahora vamos a extraer cada unno de los elemetos de una fecha
print(fechayhora.year)
print(fechayhora.month)
print(fechayhora.day)
print(fechayhora.hour)
print(fechayhora.minute)
print(fechayhora.second)
print(fechayhora.microsecond)