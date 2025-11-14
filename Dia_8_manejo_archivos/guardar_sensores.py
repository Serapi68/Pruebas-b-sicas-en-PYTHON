import csv

sensores = {'Frente': 10 ,
            'Izquierda': 20,
            'Derecha': 15}
with open('datos_sensores.csv', 'w',newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Sensor', 'Distancia'])
    for sensor, distancia in sensores.items():
        escritor.writerow([sensor, distancia])