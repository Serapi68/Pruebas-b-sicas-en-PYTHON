try:
    numero = int(input("Ingresa un número: "))
    print(10 / numero)
except ZeroDivisionError:
    print("No se puede dividir por cero.")

#try: Contiene el código que podría generar un error.
#except: Maneja el error si ocurre.
#finally: Ejecuta código siempre, ocurra o no un error (útil para cerrar recursos).
#raise: Lanza un error personalizado.

class Robot:
    
    def __init__(self,Nombre,Bateria):
        self.nombre = Nombre
        self.bateria = Bateria
        pass
    
    def saludar(self):  # Método
        print(f"Soy {self.nombre}, mi batería está al {self.bateria}%")
    
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

robot1 = Robot('Sergio', 0 )
robot1.carga()
robot1.saludar()
robot1.mover(int(input('Digite distancia que quiere recorrer: ')))