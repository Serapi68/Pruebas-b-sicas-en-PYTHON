import csv
try:
    with open('sensores.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar encabezado
        for fila in lector:
            distancia = float(fila[1])
            if distancia < 15:
                print(f"Alerta: {fila[0]} a {distancia} cm")
except FileNotFoundError:
    print("Error: El archivo sensores.csv no existe.")
except ValueError:
    print("Error: Los datos del archivo no son válidos.")