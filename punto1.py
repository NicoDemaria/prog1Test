import csv

with open('Mozos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        nombre = row[1]
        categoria = row[2]
        comision = float(row[3].replace(',', '.'))
        ventas = row[4]
        
        print(f"Nombre: {nombre}, Categoría: {categoria}, Importe a cobrar: {ventas}, Comision: {comision}%" )
