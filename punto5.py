'''5.	Se necesita un programa que muestre el total de las ventas'''

import csv
total_ventas = 0

with open('Mozos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        importe = float(row[3].replace(',', '.'))  
        total_ventas += importe

print(f"Total de ventas: {total_ventas}")
