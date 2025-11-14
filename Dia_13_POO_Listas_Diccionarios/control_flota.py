import random
import time as time 

class Robot:
    def __init__(self, nombre, bateria, modo, posicion = 0, sentido="Norte"):
        self.nombre = nombre
        self.bateria = bateria
        self.modo = modo
        self.posicion = posicion
        self.sentido = sentido
        self.sensores = {"frente": 100, "izquierda": 100, "derecha": 100}
    
    def obstaculos(self): 
        umbral = 15
        frente = self.sensores.get('frente', 100)
        izquierda = self.sensores.get('izquierda', 100)
        derecha = self.sensores.get('derecha', 100)
    
        if frente < umbral:
            if izquierda >= umbral:
                return 'girar_izquierda'
            elif derecha >= umbral:
                return 'girar_derecha'
            else:
                return 'detener'
        else:
            return 'avanzar'
    
    def consumo(self):
        if self.modo == 'Patrulla':
            return 0.2
        elif self.modo == 'Reconocimiento':
            return 0.3
        elif self.modo == 'Manual':
            return 0.1
        else:
            return 0.1
   
    def girar(self, direccion):
        sentidos = ['Norte', 'Este', 'Sur', 'Oeste']
        idx = sentidos.index(self.sentido)
        if direccion == "izquierda":
            idx = (idx - 1) % 4
        elif direccion == "derecha":
            idx = (idx + 1) % 4
        self.sentido = sentidos[idx]
        print(f'{self.nombre} gira a la {direccion} y ahora apunta hacia {self.sentido}. Batería: {self.bateria}%')
   
    def apagado(self):
        print(f'Un placer soy {self.nombre} y me queda de batería {self.bateria}%')   

    def mover(self, distancia):
        consumo_total = distancia * self.consumo()
        if self.bateria >= consumo_total:
            self.posicion += distancia
            self.bateria -= consumo_total
            print(f'{self.nombre} se ha movido {distancia} cm hacia {self.sentido}. Posición actual: {self.posicion} cm. Batería: {self.bateria:.2f}%')
        else:
            max_distancia = int(self.bateria / self.consumo())
            self.posicion += max_distancia
            self.bateria = 0
            print(f'{self.nombre} tiene muy poca batería para moverse, solo pudo moverse {max_distancia} cm. Se necesita cargar.')

#Configuracion de robots

print('Cuantos robots quieree trabajar, MAX 3 Robots:')
while True:
    try:
        x=(int(input('Cantidad de robots: ')))
        if x < 1  or x > 3:
         raise ValueError("Maximo 3 robots")
        print(f'se han escogido {x} robot(s)')
        break
    except ValueError as e:            
        print("Error:", e)


flota = []
for i in range(x):
    nombre = input(f'Digite nombre del robot {i+1}: ').capitalize()
    while True:  
        try:
            bateria = float(input(f'Batería del robot {i+1} (%): '))
            break
        except ValueError:
            print('Porfavor ingrese un dato en numeros')
    
    while True:
        try:
            y = int(input('Elige el modo de operar el robot 1=Patrulla, 0=Reconocimiento, 2=Manual: '))
            if y == 1:
                modo = 'Patrulla'
                break
            elif y == 0:
                modo = 'Reconocimiento'
                break
            elif y == 2:
                modo = 'Manual'
                break
            else:
                print('Ingrese un valor válido (0, 1, 2)')
        except ValueError:
            print('Por favor ingrese un valor válido')

    flota.append(Robot(nombre, bateria, modo))
    

# Configuracion de maniobra de robots    

for robot in flota:
    print(f'Iniciando movimiento para {robot.nombre}')

    while True:
            robot.sensores = {
                'frente': random.randint (5, 100),
                'izquierda': random.randint(5,100),
                'derecha' : random.randint(5,100)
            }
        
            
            print(f"Sensores: {robot.sensores}")
            decision = robot.obstaculos()
            

            if decision == 'avanzar':
                try:
                    distancia = int(input('Camino libre. ¿Distancia a avanzar (cm)? '))
                    robot.mover(distancia)
                except ValueError:
                    print('Distancia inválida.')
            elif decision == 'girar_izquierda':
                robot.girar('izquierda')
            elif decision == 'girar_derecha':
                robot.girar('derecha')
            else:
                print(f'{robot.nombre} está bloqueado y se detiene.')
                break

            if robot.bateria <= 0:
                print(f'{robot.nombre} sin batería. Se apaga automáticamente.')
                break

            apagar = input('¿Deseas apagar el robot? (si/no): ').strip().lower()
            if apagar == 'si':
                robot.apagado()
                break

            time.sleep(2)
        


