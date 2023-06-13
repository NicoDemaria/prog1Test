'''7.	Se necesita un programa que muestre el nombre del mozo que logró la mayor venta.'''
import csv
mayor_venta = 0
nombre_mozo = ""
with open('Mozos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        ventas = float(row[4].replace(',', '.'))  
        if ventas > mayor_venta :
            mayor_venta = ventas
            nombre_mozo = row[1]


print(f"Mayor vendedor : {nombre_mozo}")
