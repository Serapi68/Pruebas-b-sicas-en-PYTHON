class Robot:
    def __init__(self, nombre, bateria):
        self.nombre = nombre
        self.bateria = bateria
        
    def recargar(self):
        print(f'{self.nombre} se está recargando...')
        self.bateria = 100
        print(f'{self.nombre} ahora tiene batería al {self.bateria}%')
    
    def estado(self):
        carga = "BAJA" if self.bateria < 30 else ''
        return f'{self.nombre}: Batería al {self.bateria}% {carga}'
    
flota = {
    'R1' : Robot('R2D2', 80),
    'R2' : Robot('WALL-E', 22),
    'R3' : Robot('EVA', 40)
}
for id, robot in flota.items():
    print(f'ID {id}: {robot.estado()}')
    if robot.bateria < 30:
        robot.recargar()
        print(f'Nuevo estado : {robot.estado()}')
    print('---')

