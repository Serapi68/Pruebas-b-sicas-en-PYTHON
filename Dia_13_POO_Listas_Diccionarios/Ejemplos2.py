#Las listas las usaremos para robots que tengan diferentes tareas
#Los diccionarios los usaremos para setear sensores o configuracion que dependan del robot

class Robot:
    def __init__(self, nombre, bateria, sensores):
        self.nombre = nombre
        self.bateria = bateria
        self.sensores = sensores
    
    def verificar_obstaculo(self):
        return any(distancia < 15 for distancia in self.sensores.values())

flota = [
    Robot("R1", 80, {"frente": 10, "izquierda": 20}),  #Se usa una lista que sera flora con el diccionario de sensores
    Robot("R2", 90, {"frente": 25, "izquierda": 30})
]
for robot in flota:
    if robot.verificar_obstaculo():
        print(f"{robot.nombre}: Obstáculo detectado.")