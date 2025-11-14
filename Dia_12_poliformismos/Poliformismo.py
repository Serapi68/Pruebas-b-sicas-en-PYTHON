class Robot:
    def actuar(self):
        print("Realizando acción genérica")

class RobotMovil(Robot):
    def actuar(self):
        print("Moviéndome por el entorno")

class RobotCamara(Robot):
    def actuar(self):
        print("Capturando imágenes")

robots = [RobotMovil(), RobotCamara()]
for robot in robots:
    robot.actuar()  # Imprime diferentes acciones