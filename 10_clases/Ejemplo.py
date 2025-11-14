class Robot:
    def __init__(self, nombre, bateria): #__init__ herramienta de python
        self.nombre = nombre  # Atributo
        self.bateria = bateria

    def saludar(self):  # Método
        print(f"Soy {self.nombre}, mi batería está al {self.bateria}%")

robot1 = Robot(input('¿Cual es mi nombre?: '), 80)  # Crear objeto
robot1.saludar()  # Imprime: Soy Explorador, mi batería está al 80%

class Robot:
    def __init__(self, nombre, bateria):
        self.nombre = nombre
        self.bateria = bateria
        self.sensores = {"frente": 100, "izquierda": 100, "derecha": 100}
    
    def saludar(self):  # Método
        print(f"Soy {self.nombre}, mi batería está al {self.bateria}%")
    
    def verificar_obstaculo(self):      
        for sensor, distancia in self.sensores.items():
            if distancia < 15:
                return f"Detener: obstáculo cerca en sensor de  {sensor}."
        return "Avanzar."

robot1 = Robot("R2D2", 90)
robot1.saludar()
robot1.sensores["izquierda"] = 30
print(robot1.verificar_obstaculo())  # Imprime: Detener: obstáculo cerca.