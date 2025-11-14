import numpy as np 
import csv

posiciones = np.array ([0,5,20,25,30])
diferencias = np.diff(posiciones)
print('Distancia recorrida en cm: ', diferencias)
for i in range(len(posiciones)) :
     print('Posicion: ', i + 1, ':', posiciones[i], 'cm' )
print('Distancia total recorrida: ', np.sum(diferencias))
if np.any(diferencias>10):
    brusco = np.where(diferencias > 10)[0]
    for i in brusco:    
        print('Ha habido un cambio de posicion bruco entre posicion: ', i + 1, 'y', i+2 )

with open('trayectoria.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Posicion', 'Diferencia de Distancia'])
    for i, pos in enumerate(posiciones):
        diff = diferencias[i] if i < len(diferencias) else 0
        escritor.writerow([pos, diff])
    if brusco.size > 0:
        escritor.writerow([])
        escritor.writerow(['Ha habido un cambio de posicion brusco:'])
        for i in brusco:
            escritor.writerow([f'Entre posicion: {i+1} y {i+2} '])
