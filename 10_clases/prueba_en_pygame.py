import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulación Robot")

font = pygame.font.SysFont(None, 24)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

class Robot:
    def __init__(self, nombre, bateria, modo, posicion, sentido="Norte"):
        self.nombre = nombre
        self.bateria = bateria
        self.modo = modo
        self.posicion = posicion  # posición x, y en pantalla
        self.sentido = sentido
        self.sensores = {"frente": 100, "izquierda": 100, "derecha": 100}
    
    def obstaculos(self): 
        umbral = 50  # Ajustado a escala visual
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
    
    def consumo(self):
        if self.modo == 'Patrulla':
            return 0.05
        elif self.modo == 'Reconocimiento':
            return 0.07
        elif self.modo == 'Manual':
            return 0.03
        else:
            return 0.03
   
    def girar(self, direccion):
        sentidos = ["Norte", "Este", "Sur", "Oeste"]
        idx = sentidos.index(self.sentido)
        if direccion == "izquierda":
            idx = (idx - 1) % 4
        elif direccion == "derecha":
            idx = (idx + 1) % 4
        self.sentido = sentidos[idx]
    
    def mover(self, distancia):
        consumo_total = distancia * self.consumo()
        if self.bateria >= consumo_total:
            # Movimiento según dirección
            if self.sentido == "Norte":
                self.posicion[1] -= distancia
            elif self.sentido == "Este":
                self.posicion[0] += distancia
            elif self.sentido == "Sur":
                self.posicion[1] += distancia
            elif self.sentido == "Oeste":
                self.posicion[0] -= distancia
            
            self.bateria -= consumo_total
        else:
            # Mueve lo máximo posible con batería restante
            max_distancia = int(self.bateria / self.consumo())
            if self.sentido == "Norte":
                self.posicion[1] -= max_distancia
            elif self.sentido == "Este":
                self.posicion[0] += max_distancia
            elif self.sentido == "Sur":
                self.posicion[1] += max_distancia
            elif self.sentido == "Oeste":
                self.posicion[0] -= max_distancia
            self.bateria = 0
    
    def actualizar_sensores(self):
        # Simula sensores con valores aleatorios
        self.sensores['frente'] = random.randint(10, 100)
        self.sensores['izquierda'] = random.randint(30, 100)
        self.sensores['derecha'] = random.randint(60, 100)

def dibujar_robot(robot):
    # Dibuja el robot (un rectángulo con una "flecha" para sentido)
    x, y = robot.posicion
    pygame.draw.rect(screen, BLUE, (x-15, y-15, 30, 30))
    
    # Dibuja una flecha indicando el sentido
    if robot.sentido == "Norte":
        pygame.draw.polygon(screen, WHITE, [(x, y-20), (x-10, y-10), (x+10, y-10)])
    elif robot.sentido == "Este":
        pygame.draw.polygon(screen, WHITE, [(x+20, y), (x+10, y-10), (x+10, y+10)])
    elif robot.sentido == "Sur":
        pygame.draw.polygon(screen, WHITE, [(x, y+20), (x-10, y+10), (x+10, y+10)])
    elif robot.sentido == "Oeste":
        pygame.draw.polygon(screen, WHITE, [(x-20, y), (x-10, y-10), (x-10, y+10)])

def mostrar_info(robot):
    lines = [
        f"Nombre: {robot.nombre}",
        f"Batería: {robot.bateria:.2f}%",
        f"Modo: {robot.modo}",
        f"Posición: {robot.posicion}",
        f"Sentido: {robot.sentido}",
        "Sensores:",
        f"  Frente: {robot.sensores['frente']}",
        f"  Izquierda: {robot.sensores['izquierda']}",
        f"  Derecha: {robot.sensores['derecha']}"
    ]
    y = 10
    for line in lines:
        text = font.render(line, True, WHITE)
        screen.blit(text, (10, y))
        y += 20

def main():
    clock = pygame.time.Clock()
    nombre = input("Define mi nombre: ")
    
    while True:
        try:
            bateria = int(input("¿En qué porcentaje está mi batería?: "))
            break
        except ValueError:
            print("Por favor ingrese un número válido")
    
    while True:
        try:
            modo_in = int(input("Elige el modo de operar el robot 1=Patrulla, 0=Reconocimiento, 2=Manual: "))
            if modo_in == 1:
                modo = 'Patrulla'
                break
            elif modo_in == 0:
                modo = 'Reconocimiento'
                break
            elif modo_in == 2:
                modo = 'Manual'
                break
            else:
                print("Ingrese un valor válido (0, 1, 2)")
        except ValueError:
            print("Por favor ingrese un valor válido")
    
    robot = Robot(nombre, bateria, modo, [WIDTH//2, HEIGHT//2])

    avanzar_distancia = 10  # cantidad fija para avanzar cada ciclo

    running = True
    while running:
        screen.fill(BLACK)
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Actualiza sensores y decide qué hacer
        robot.actualizar_sensores()
        decision = robot.obstaculos()

        if decision == 'avanzar':
            robot.mover(avanzar_distancia)
        elif decision == 'girar_izquierda':
            robot.girar('izquierda')
        elif decision == 'girar_derecha':
            robot.girar('derecha')
        else:
            print(f'{robot.nombre} está bloqueado y se detendrá.')
            running = False
        
        if robot.bateria <= 0:
            print(f'Batería agotada. {robot.nombre} se apagará automáticamente.')
            running = False
        
        # Dibujar robot y datos
        dibujar_robot(robot)
        mostrar_info(robot)
        
        pygame.display.flip()
        clock.tick(2)  # 2 FPS para ver bien cada paso

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
