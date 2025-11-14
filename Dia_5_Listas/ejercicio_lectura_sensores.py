sensores = [10, 15, 30, 25, 12]
promedio = sum(sensores) / len(sensores)
for i in range(len(sensores)):
    print('Sensor', i+1, ':', sensores[i], 'cm')
print('El promedio de lecturas del sensor: ', promedio, 'cm')