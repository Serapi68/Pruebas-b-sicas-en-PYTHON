class Robot:
    def __init__(self, nombre, bateria):
        self.nombre = nombre
        self.bateria = bateria
        
    def saludar(self):
        print(f'Hola soy {self.nombre} mi bateria tiene {self.bateria}% de carga')

    def verificar_bateria(self):
        return self.bateria < 15

flota = [
    Robot('R1', 80),
    Robot('R2', 90),
    Robot('R3', 12)
]

for robot in flota:
    robot.saludar()
    if robot.verificar_bateria():
        print(f'{robot.nombre} bateria baja. : {robot.bateria}%')
