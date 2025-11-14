import csv
from datetime import datetime

def obstaculos (sensores): #Programacion de maniobra de esquive
    umbral = 15

    frente = sensores.get('frente', 100)
    izquierda = sensores.get('izquierda', 100)
    derecha = sensores.get('derecha', 100)
    
    if frente < umbral:
        if izquierda >= umbral:
            return 'Obstaculo al frente. Girar a la izquierda.'
        elif derecha >= umbral:
            return 'Obstaculo al frente. Girar a la derecha.'
        else:
            return 'Obstaculo en todas las direcciones. Detener robot.'
    else:
        return 'Camino despejado. Avanzar robot.'

sensores = [
    {'Sensor': 'frente', 'Distancia': 12, 'Tiempo': 1,},
    {'Sensor': 'Izquierda', 'Distancia': 12, 'Tiempo': 2},
    {'Sensor': 'Derecha', 'Distancia': 18, 'Tiempo': 3}
    ]



with open('reto_sensores.csv', 'w', newline= '') as archivo :
    escritor = csv.writer(archivo)
    escritor.writerow(['Sensores', 'Distancia', 'Tiempo'])
    for lectura in sensores :
        escritor.writerow([lectura['Sensor'], lectura['Distancia'], lectura['Tiempo']])
#se crea un nuevo diccionario para la lectura de lo demas
lectura ={}

with open('reto_sensores.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    next(lector)  #saltar encabezado
    for fila in lector:
        sensor = fila[0].lower( )
        distancia = int(fila[1])
        tiempo = int(fila[2])
        lectura[sensor] = distancia
        if distancia < 15:
            print(f"Alerta: {fila[0]} a {distancia} cm en tiempo {fila[2]}")

ahora = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

decision = obstaculos(lectura)
print (decision)

with open('reto_sensores.csv', 'a', newline= '') as archivo :
    escritor = csv.writer(archivo)
    escritor.writerow([])
    escritor.writerow(['Decision de movimiento: '])
    escritor.writerow([ahora])
    escritor.writerow([])
    escritor.writerow([decision])