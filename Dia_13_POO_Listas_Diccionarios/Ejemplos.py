class Robot:
    def __init__(self, nombre, bateria):
        self.nombre = nombre
        self.bateria = bateria
    
    def estado(self):
        return f"{self.nombre}: {self.bateria}%"

flota = [Robot("R1", 80), Robot("R2", 90)] #Lista de robots
for robot in flota:
    print(robot.estado())

flota = {                   #Este diccionario pone al 'R1' como claves y lo demas son sus objetos o configuraciones
    "R1": Robot("R1", 80),
    "R2": Robot("R2", 90)
}
print(flota["R1"].estado())
print(flota["R2"].estado())