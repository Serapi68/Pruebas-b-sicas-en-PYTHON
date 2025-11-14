import csv

with open('reto_sensores.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        if not fila:
            continue
        if 'INFO_ROBOT' in fila[0]:
            seccion = 'info'
        elif 'DATA_SENSORES' in fila[0]:
            seccion = 'data'
        elif 'Decision de movimiento' in fila[0]:
            seccion = 'decision'
        if seccion == 'info':
            if len(fila) >= 2:
                print(f"{fila[0].replace(':', '')}: {fila[1]}")
        elif seccion == 'sensores':
            if fila[0].lower() == 'sensores':
                print(f"{'Sensor':<10} {'Distancia':<10} {'Tiempo':<10}")
            elif len(fila) == 3:
                print(f"{fila[0]:<10} {fila[1]:<10} {fila[2]:<10}")
        elif seccion == 'decision':
            print(fila[0])