

# VAmos a importar un archivo CSV para tratarlo con python
import csv

with open(r'C:\Users\Hp\Desktop\lp3\semana5\Global_Mobility_Report.csv',encoding="utf8") as f:
    datos = csv.reader(f, delimiter=',')
    for fila in datos:
        print(f"{fila[0]}\t {fila[1]}\t {fila[2]}\t {fila[3]}\t {fila[4]}\t {fila[5]}\t {fila[6]}\t {fila[7]}\t {fila[8]}\t {fila[9]}\t {fila[10]} ")









