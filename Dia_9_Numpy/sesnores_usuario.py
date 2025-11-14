import numpy as np
import csv

sensores = {'frente': 0, 'izquierda': 0, 'derecha': 0}
for sensor in sensores:
    sensores[sensor] = float(input(f"Distancia de {sensor} (cm): "))
valores = np.array(list(sensores.values()))
print("Promedio:", np.mean(valores))
print("Mínimo:", np.min(valores))
with open('sensor_log.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Sensor', 'Distancia'])
    for sensor, distancia in sensores.items():
        escritor.writerow([sensor, distancia])