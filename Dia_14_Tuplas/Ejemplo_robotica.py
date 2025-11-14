class Robot:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion  # Tupla (x, y)
        self.modos_validos = {"Patrulla", "Reconocimiento", "Manual"}  # Conjunto
    
    def cambiar_modo(self, modo):
        if modo in self.modos_validos:
            print(f"{self.nombre} cambió a {modo}")
        else:
            raise ValueError("Modo no válido")

robot1 = Robot("Rover", (10, 20))
robot1.cambiar_modo("Patrulla")
print(f"Posición: {robot1.posicion}")