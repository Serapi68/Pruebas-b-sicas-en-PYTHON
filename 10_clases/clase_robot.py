class Robot:
    def __init__(self,nombre, bateria, modo):
        
        self.nombre = nombre
        self.bateria = bateria
        self.modo = modo
    def saludar(self):
        print(f'Hola soy {self.nombre}, mi bateria esta ha {self.bateria}%, y estoy en entorno de funcionamiento de {self.modo}')

robot1 = Robot('','','')

robot1.nombre = input('Define mi nombre: ')
robot1.bateria = input('¿En que porcentaje esta mi bateria?: ')


while True:
    try:
        x = int(input('Elige el modo de operar el robot 1=Patrulla, 0=Reconocimiento, 2=Manual: '))
        if x == 1 :
            robot1.modo = 'Patrulla' 
            
            break
        elif x == 2 :
            robot1.modo = 'Manual'
            
            break
        elif x== 0 :
            robot1.modo = 'Reconocimiento' 
            
            break
        else:
            print('Ingrese un valor valido(0, 1, 2)')
    except ValueError :
        print('Porfavor ingrese un valor valido')

robot1.saludar()