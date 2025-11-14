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
    
robot={}
robot['Nombre'] = input('Digita nombre del robot: ').capitalize()
robot['Bateria'] = int(input('Digita bateria del robot: '))
alerta = ''
if robot['Bateria'] < 20 : 
    alerta = f'ALERTA!!!! ME ESTOY MURIENOD BATERIA = {robot["Bateria"]}%'
    print (alerta)

while True:
    try:
        x = int(input('Elige el modo de operar el robot 1=Patrulla, 0=Reconocimiento, 2=Manual: '))
        if x == 1 :
            robot['modo'] = 'Patrulla' 
            
            break
        elif x == 2 :
            robot ['modo'] = 'Manual'
            
            break
        elif x== 0 :
            robot ['modo'] = 'Reconocimiento' 
            
            break
        else:
            print('Ingrese un valor valido(0, 1, 2)')
    except ValueError :
        print('Porfavor ingrese un valor valido')


sensores = []
for sensor in ['frente', 'izquierda', 'derecha']:
    distancia = int(input(f'Digite distancia del sensor {sensor}: '))
    tiempo = int(input('Digite tiempo de scan: '))
    sensores.append({'sensor': sensor, 'distancia': distancia, 'tiempo': tiempo})


with open('reto_sensores.csv', 'w', newline= '') as archivo :
    escritor = csv.writer(archivo)
    escritor.writerow(['INFO_ROBOT: '])
    escritor.writerow([])
    for clave, valor in robot.items():
        escritor.writerow([f'{clave}:', valor] )    
    escritor.writerow([])
    if alerta:
        escritor.writerow([])
        escritor.writerow([alerta])
        escritor.writerow(['Para proxima conectar cargador'])
        escritor.writerow([])
    escritor.writerow(['DATA_SENSORES:'])
    escritor.writerow([])
    escritor.writerow(['Sensores', 'Distancia', 'Tiempo'])
    for lectura in sensores :
        escritor.writerow([lectura['sensor'], lectura['distancia'], lectura['tiempo']])
#se crea un nuevo diccionario para la lectura de lo demas
lectura ={}

with open('reto_sensores.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    
    for fila in lector:
        if fila == ['Sensores', 'Distancia', 'Tiempo']:
            break
        

    lectura = {}
    for fila in lector:
        if len(fila) != 3:
            continue  
        sensor = fila[0].lower()
        distancia = int(fila[1])
        tiempo = int(fila[2])
        lectura[sensor] = distancia
        if distancia < 15:
            print(f"Alerta: {fila[0]} a {distancia} cm en tiempo {fila[2]}")
        

ahora = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

decision = obstaculos(lectura)

with open('reto_sensores.csv', 'a', newline= '') as archivo :
    escritor = csv.writer(archivo)
    escritor.writerow([])
    escritor.writerow(['Decision de movimiento: '])
    escritor.writerow([ahora])
    escritor.writerow([])
    escritor.writerow([decision])