sensores = {"Al frente": 10, "Derecha": 22, "Izquierda": 18}
for sensor, distancia in sensores.items():
    print(f"Sensor {sensor}: {distancia} cm")

for sensor, distancia in sensores.items():
    if distancia < 15:
        print(f"¡Alerta! Obstáculo cerca en sensor {sensor}: {distancia} cm")
    else:
        print(f"Sensor {sensor}: {distancia} cm")