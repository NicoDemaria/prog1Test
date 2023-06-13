
import csv

categoria_usuario = input("Ingrese la categoría deseada: ")

with open('Mozos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    with open('Listado_Mozos_Categoria.csv', 'w', newline='') as nuevoArchivo:
        escribirNuevo = csv.writer(nuevoArchivo)
        escribirNuevo.writerow(['Nombre', 'Categoría'])
        for row in reader:
            nombre = row[1]
            categoria = row[2]
            if categoria == categoria_usuario:
                escribirNuevo.writerow([nombre, categoria])
