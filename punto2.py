import csv

categoria_usuario = input("Ingrese la categoría deseada: ")

with open('Mozos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        nombre = row[1]
        categoria = row[2]
        if categoria == categoria_usuario:
            print(f"Nombre: {nombre}, Categoría: {categoria}")
