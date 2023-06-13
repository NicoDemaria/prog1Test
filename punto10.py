'''10.	Se necesita un programa que muestre el mayor importe a pagar por comisiones de ventas.'''

import csv

mayorComision = 0
with open('Mozos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        ventas = float(row[4].replace(',', '.'))  
        comisiones = float(row[3].replace(',', '.')) /100
        totalComisiones = ventas * comisiones
        if totalComisiones > mayorComision :
            mayorComision = totalComisiones
        
        


print(f"Mayor comision: {mayorComision}")
