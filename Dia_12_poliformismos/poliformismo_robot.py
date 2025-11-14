class Robot:
    def __init__(self,nombre,bateria):
        self.nombre = nombre
        self.bateria = bateria
    
    def actuar(self):
        print(f'{self.nombre} realizando accion generica')
    
    def consumo(self, cantidad):
        if self.bateria >= cantidad:
            self.bateria -= cantidad
            return True
        else:
            print(f'{self.nombre} Bateria Insuficiente' )

class RobotMovil(Robot):

    def actuar(self):
        if self.consumo(12) :
         print(f'{self.nombre}: Moviendome por el entorno, Bateria: {self.bateria}%')

class RobotCamara(Robot):

    def actuar(self):
        if self.consumo(5) :
            print(f'{self.nombre}: Vigilando y capturando imagen, Bateria: {self.bateria}%')

robots = [RobotMovil('Milito', 13), RobotCamara('Camarita', 90)]

for robot in robots :
    robot.actuar()