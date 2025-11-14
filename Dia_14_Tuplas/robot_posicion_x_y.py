import random
import csv
class Robot:
    def __init__(self, nombre, posicion, modo):
        self.nombre = nombre
        self.posicion = posicion  # Tupla (x, y)
        self.modos_validos = {"Patrulla", "Reconocimiento", "Manual"}
        self.modo = modo if modo in self.modos_validos else "Manual"
        self.sensores = {"frente", "izquierda", "derecha"}
        self.lecturas = {}
    
    def actualizar_sensores(self):
        for sensor in self.sensores:
            self.lecturas[sensor] = random.randint(5, 100)
    
    def decidir_accion(self):
        if any(self.lecturas[sensor] < 15 for sensor in self.sensores):
            return f"{self.nombre}: Obstáculo cerca."
        return f"{self.nombre}: Avanzar."
    
    def guardar_estado(self):
        with open('flota.csv', 'a', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([self.nombre, self.posicion[0], self.posicion[1], self.modo, self.lecturas.get('frente', 100)])

flota = []
for i in range(2):
    nombre = input(f"Nombre del robot {i+1}: ").capitalize()
    x = float(input(f"Coordenada x para {nombre}: "))
    y = float(input(f"Coordenada y para {nombre}: "))
    modo = input(f"Modo para {nombre} (Patrulla/Reconocimiento/Manual): ").capitalize()
    robot = Robot(nombre, (x, y), modo)
    robot.actualizar_sensores()
    flota.append(robot)

with open('flota.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Nombre', 'X', 'Y', 'Modo', 'Frente'])

for robot in flota:
    print(f"{robot.nombre}: {robot.decidir_accion()}")
    robot.guardar_estado()