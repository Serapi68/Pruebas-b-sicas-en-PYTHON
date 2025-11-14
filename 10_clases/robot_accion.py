import random

class Robot:
    def __init__(self, nombre, bateria, modo, posicion, sentido="Norte"):
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
        sentidos = ["Norte", "Este", "Sur", "Oeste"]
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


robot1 = Robot('', 0, '', 0)

robot1.nombre = input('Define mi nombre: ')
while True:  
    try:
        robot1.bateria = int(input('¿En qué porcentaje está mi batería?: '))
        break
    except ValueError:
        print('Porfavor ingrese un dato en numeros')

 
while True:
    try:
        x = int(input('Elige el modo de operar el robot 1=Patrulla, 0=Reconocimiento, 2=Manual: '))
        if x == 1:
            robot1.modo = 'Patrulla'
            break
        elif x == 0:
            robot1.modo = 'Reconocimiento'
            break
        elif x == 2:
            robot1.modo = 'Manual'
            break
        else:
            print('Ingrese un valor válido (0, 1, 2)')
    except ValueError:
        print('Por favor ingrese un valor válido')


while True:
    try:

        robot1.sensores['frente'] = random.randint(5, 100)
        robot1.sensores['izquierda'] = random.randint(5, 100)
        robot1.sensores['derecha'] = random.randint(5, 100)
        print('Lectura de sensores: ')
        for clave in robot1.sensores:
            print(clave, ':', robot1.sensores[clave])

        decision = robot1.obstaculos()

        if decision == 'avanzar':
            distancia = int(input('Camino despejado, ¿a qué distancia quieres avanzar (cm)? '))
            robot1.mover(distancia)
        elif decision == 'girar_izquierda':
            robot1.girar('izquierda')
        elif decision == 'girar_derecha':
            robot1.girar('derecha')
        else:
            print(f'{robot1.nombre} está bloqueado y se detendrá.')
            break

        if robot1.bateria <= 0:
            print(f'Batería agotada. {robot1.nombre} se apagará automáticamente.')
            break

        apagar = input('¿Deseas apagar el robot? (si/no): ').strip().lower()
        if apagar == 'si':
            robot1.apagado()
            break

    except ValueError:
        print('Por favor ingrese una distancia válida en números')
