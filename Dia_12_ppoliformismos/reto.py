import random
class Robot:
    def __init__(self, nombre, bateria):
        if not isinstance(bateria, (int, float)) or bateria < 0 or bateria > 100:
            raise ValueError("Batería debe estar entre 0 y 100.")
        self.nombre = nombre
        self.bateria = bateria
        self.sensores = {"frente": 100, "izquierda": 100, "derecha": 100}
    
    def actualizar_sensores(self):
        for sensor in self.sensores:
            self.sensores[sensor] = random.randint(5, 100)
    
    def decidir_accion(self):
        if self.sensores["frente"] < 15:
            return f"Detener {self.nombre}: obstáculo cerca."
        return f"{self.nombre} puede avanzar."

class RobotMovil(Robot):
    def __init__(self, nombre, bateria, posicion):
        super().__init__(nombre, bateria)
        self.posicion = posicion
    
    def decidir_accion(self):
        if self.bateria < 10:
            return f"{self.nombre}: Batería baja, recargar."
        return super().decidir_accion()
    
    def mover(self, distancia):
        if distancia < 0:
            raise ValueError("Distancia no puede ser negativa.")
        self.posicion += distancia
        self.bateria -= distancia * 0.2
        return f"{self.nombre} se movió a {self.posicion} cm"

try:
    robot1 = RobotMovil(input("Nombre del robot: ").capitalize(), 80, 0)
    robot1.actualizar_sensores()
    print("Sensores:", robot1.sensores)
    print(robot1.decidir_accion())
    if "puede avanzar" in robot1.decidir_accion():
        robot1.mover(float(input("Distancia a mover (cm): ")))
except ValueError as e:
    print(f"Error: {e}")