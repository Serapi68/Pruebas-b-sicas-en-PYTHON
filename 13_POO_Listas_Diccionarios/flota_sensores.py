class Robot:
    def __init__(self, nombre, bateria):
        self.nombre = nombre
        self.bateria = bateria
        self.sensores = {'frente': 100, 'izquierda': 100, 'derecha': 100}
    
    def obstaculos(self): 
        umbral = 15
        frente = self.sensores.get('frente', 100)
        izquierda = self.sensores.get('izquierda', 100)
        derecha = self.sensores.get('derecha', 100)
    
        if frente < umbral:
            if izquierda >= umbral:
                return 'girar_izquierda'
            elif derecha >= umbral:
                return 'girar_derecha'
            else:
                return 'detener'
        else:
            return 'avanzar'

class RobotMovil(Robot):

    def __init__(self, nombre, bateria, posicion):
        super().__init__(nombre, bateria)
        self.posicion = posicion

    def mover(self, distancia):
        consumo = distancia * 0.5
        try:
            if self.bateria < consumo:
                raise ValueError("Batería agotada.")
            self.bateria -= consumo
            print(f"{self.nombre} se movió {distancia} cm. Batería: {self.bateria}%")
        except ValueError as e:
            print(f"Error: {e}")

flota =  [RobotMovil('R1', 80, 0),
          RobotMovil('R2', 90, 10)]

flota[0].sensores['frente'] = 10

for robot in flota:
    accion = robot.obstaculos()
    if accion != 'avanzar':
        print(f"{robot.nombre}: Obstáculo cerca. - Accion: {accion}")
    else:
        robot.mover(20)