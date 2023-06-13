'''8.	Se necesita un programa que muestre el total a pagar por comisiones de ventas.'''

import csv

totalComisiones = 0

with open('Mozos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        ventas = float(row[4].replace(',', '.'))  
        comisiones = float(row[3].replace(',', '.')) /100
        totalComisiones += ventas * comisiones
        


print(f"Total de Comisiones : {totalComisiones}")
