class Robot:
   
    def __init__(self,nombre, bateria):
        self.nombre = nombre
        self.bateria = bateria
   
    def saludar(self):
        print(f'Hola soy {self.nombre} y mi bateria esta al {self.bateria}%')
    
class RobotMovil(Robot):
    
    def __init__(self, nombre, bateria, posicion ):
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

robot1 = RobotMovil('Milito', 80, 0)
robot1.saludar()
robot1.mover(23)


        