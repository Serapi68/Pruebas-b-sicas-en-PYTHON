import csv

sensores = {'front': 10, 'left': 25, 'right': 30}
with open('sensores.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Sensor', 'Distancia'])
    for sensor, distancia in sensores.items():
        escritor.writerow([sensor, distancia])