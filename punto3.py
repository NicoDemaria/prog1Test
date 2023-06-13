import csv

with open('Mozos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    with open('Listado_Mozos.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Nombre', 'Categoría', 'Importe a cobrar'])
        for row in reader:
            nombre = row[1]
            categoria = row[2]
            comision = float(row[3].replace(',', '.'))
            ventas = float(row[4])
            porcentaje = comision / 100
            dineroTotal = ventas * porcentaje
            writer.writerow([nombre, categoria, 'Total a Cobrar: ',dineroTotal])
