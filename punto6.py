'''6.	Se necesita un programa que muestre el promedio de las ventas.'''

import csv
total_ventas = 0

with open('Mozos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        ventas = float(row[4].replace(',', '.'))  
        total_ventas += ventas

promedio_ventas = total_ventas / 7

print(f"Promedio de ventas: {promedio_ventas}")
