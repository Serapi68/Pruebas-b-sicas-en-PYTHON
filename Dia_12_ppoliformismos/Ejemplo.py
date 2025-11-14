class Robot: #Clase padre
    def __init__(self, nombre, bateria):
        self.nombre = nombre
        self.bateria = bateria
    
    def saludar(self):
        print(f"Soy {self.nombre}, batería al {self.bateria}%")

class RobotMovil(Robot): #RobotMovil es clase hija
    def mover(self, distancia):
        print(f"{self.nombre} se mueve {distancia} cm")

class RobotCamara(Robot): ##Otra clase hija
    def camara(self, resolucion) :
        print(f'{self.nombre} tiene una resolucion de {resolucion} pixeles')
robot1 = RobotMovil("Rover", 80)
robot2 = RobotCamara('Camarita', 98)
robot1.saludar()  # Imprime: Soy Rover, batería al 80%
robot1.mover(10)  # Imprime: Rover se mueve 10 cm
robot2.saludar()    
robot2.camara(720)