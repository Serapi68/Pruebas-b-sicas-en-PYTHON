import csv

robot = {'Nombre': 'Prototipo V1', 'Bateria': 80, 'modo': 'Patrulla'}
with open ('configuracion_robot', 'w') as archivo:
    for clave, valor in robot.items(): 
        archivo.write(f'{clave}: {valor}\n') 

with open ('configuracion_robot', 'r') as archivo:
    for linea in archivo :
        print(linea.strip()) #strip elimina salto de linea

