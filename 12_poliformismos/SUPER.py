class Robot:
    def __init__(self, nombre, bateria):
        self.nombre = nombre
        self.bateria = bateria
    
    def verificar_bateria(self):
        return f"Batería al {self.bateria}%"

class RobotMovil(Robot):
    def __init__(self, nombre, bateria, posicion):
        super().__init__(nombre, bateria)
        self.posicion = posicion
    
    def verificar_bateria(self):
        return f"{self.nombre}: Batería al {self.bateria}%, posición {self.posicion} cm"

robot1 = RobotMovil("Rover", 80, 0)
print(robot1.verificar_bateria())  # Imprime: Rover: Batería al 80%, posición 0 cm