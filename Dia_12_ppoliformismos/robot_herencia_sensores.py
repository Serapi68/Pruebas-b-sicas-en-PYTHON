class Robot:
    def __init__(self, nombre, bateria):

        self.nombre = nombre
        self.bateria = bateria
        self.sensores = {'frente': 100, 'Izquierda': 100, 'Derecha': 100}
    
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

class RobotMovil(Robot) :

    def __init__(self, nombre, bateria, posicion):
        super().__init__(nombre, bateria)
        self.posicion = posicion

    def carga (self):
        while True:
            try:
                bateria = int(input("Ingresa nivel de batería: "))
                if bateria < 0 or bateria > 100 :
                    raise ValueError("La batería tiene que ser entre 0 y 100.")
                print (f'Nivel de bateria: {bateria}%')
                self.bateria = bateria
                break
            except ValueError as e:
                print("Error:", e)
            finally:
                print("Verificación completada.")
    
    def mover(self, distancia):
        consumo = distancia * 0.5
        try:
            if self.bateria < consumo:
                raise ValueError("Batería agotada.")
            self.bateria -= consumo
            print(f"{self.nombre} se movió {distancia} cm. Batería: {self.bateria}%")
        except ValueError as e:
            print(f"Error: {e}") 

robot1 = RobotMovil('Milito', 100, 0)
robot1.sensores['frente'] = 10

print(robot1.obstaculos())
robot1.mover(10)