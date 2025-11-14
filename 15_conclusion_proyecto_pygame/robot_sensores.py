import pygame
import sys
import time

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Robot")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)

# Fuentes
try:
    font = pygame.font.SysFont('Arial', 24)
    small_font = pygame.font.SysFont('Arial', 18)
    input_font = pygame.font.SysFont('Arial', 22)
except:
    font = pygame.font.Font(None, 24)
    small_font = pygame.font.Font(None, 18)
    input_font = pygame.font.Font(None, 22)

class RobotSimulator:
    def __init__(self):
        self.estado = 0  # 0=Apagado, 1=Encendido
        self.distancia = 0
        self.direccion = 0  # 0=Izquierda, 1=Derecha
        self.pos_x = WIDTH // 2
        self.pos_y = HEIGHT // 2
        self.angulo = 0
        self.mensaje = "Bienvenido al Simulador de Robot"
        
    def dibujar_robot(self):
        # Dibujar el robot (triángulo que apunta en la dirección actual)
        direction = pygame.math.Vector2(1, 0).rotate(self.angulo)
        left_dir = pygame.math.Vector2(-1, -0.5).rotate(self.angulo)
        right_dir = pygame.math.Vector2(-1, 0.5).rotate(self.angulo)
        
        points = [
            (self.pos_x + 30 * direction.x, self.pos_y + 30 * direction.y),
            (self.pos_x + 20 * left_dir.x, self.pos_y + 20 * left_dir.y),
            (self.pos_x + 20 * right_dir.x, self.pos_y + 20 * right_dir.y)
        ]
        pygame.draw.polygon(screen, BLUE, points)
        
        # Dibujar sensor de distancia
        if self.estado == 1 and self.distancia > 0:
            max_dist = min(self.distancia * 10, 300)
            end_pos = (self.pos_x + max_dist * direction.x, 
                      self.pos_y + max_dist * direction.y)
            pygame.draw.line(screen, RED, (self.pos_x, self.pos_y), end_pos, 2)
            
            # Mostrar distancia
            text = small_font.render(f"{self.distancia:.1f}m", True, BLACK)
            screen.blit(text, (end_pos[0] + 10, end_pos[1]))

    def actualizar_posicion(self):
        if self.estado == 1 and self.distancia > 5:
            # Mover hacia adelante
            direction = pygame.math.Vector2(1, 0).rotate(self.angulo)
            self.pos_x += 5 * direction.x
            self.pos_y += 5 * direction.y
            self.distancia -= 0.5
            
            # Limitar a los bordes de la pantalla
            self.pos_x = max(30, min(WIDTH - 30, self.pos_x))
            self.pos_y = max(30, min(HEIGHT - 30, self.pos_y))

    def girar(self, direccion):
        if direccion == 1:  # Derecha
            self.angulo -= 90
        else:  # Izquierda
            self.angulo += 90
        self.mensaje = f"Girando a {'derecha' if direccion == 1 else 'izquierda'}"

def dibujar_interfaz(robot, input_text, input_prompt):
    # Fondo
    screen.fill(WHITE)
    
    # Área de información superior
    pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, WIDTH, 80))
    pygame.draw.line(screen, GRAY, (0, 80), (WIDTH, 80), 2)
    
    # Área de entrada inferior
    pygame.draw.rect(screen, LIGHT_GRAY, (0, HEIGHT-100, WIDTH, 100))
    pygame.draw.line(screen, GRAY, (0, HEIGHT-100), (WIDTH, HEIGHT-100), 2)
    
    # Mostrar estado del robot
    estado_text = f"Estado: {'Encendido' if robot.estado == 1 else 'Apagado'}"
    estado_surf = font.render(estado_text, True, BLACK)
    screen.blit(estado_surf, (20, 20))
    
    if robot.estado == 1:
        dist_surf = font.render(f"Distancia: {robot.distancia:.1f}m", True, BLACK)
        screen.blit(dist_surf, (20, 50))
    
    # Mostrar mensaje del sistema
    mensaje_surf = small_font.render(robot.mensaje, True, BLACK)
    screen.blit(mensaje_surf, (WIDTH//2 - mensaje_surf.get_width()//2, HEIGHT-80))
    
    # Mostrar prompt de entrada
    prompt_surf = input_font.render(input_prompt, True, BLACK)
    screen.blit(prompt_surf, (20, HEIGHT-70))
    
    # Dibujar cuadro de entrada de texto
    input_rect = pygame.Rect(20, HEIGHT-40, WIDTH-40, 30)
    pygame.draw.rect(screen, WHITE, input_rect, 0)
    pygame.draw.rect(screen, BLACK, input_rect, 2)
    
    # Mostrar texto ingresado
    text_surf = input_font.render(input_text, True, BLACK)
    screen.blit(text_surf, (input_rect.x + 5, input_rect.y + 5))
    
    return input_rect

def main():
    clock = pygame.time.Clock()
    robot = RobotSimulator()
    input_text = ""
    input_prompt = "Presione E para encender (1) o S para salir (2)"
    current_mode = "estado"  # estado, distancia, continuar, direccion
    
    running = True
    while running:
        input_rect = dibujar_interfaz(robot, input_text, input_prompt)
        robot.dibujar_robot()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        if current_mode == "estado":
                            robot.estado = int(input_text)
                            if robot.estado == 1:
                                current_mode = "distancia"
                                input_prompt = "Ingrese distancia al obstáculo (metros):"
                                robot.mensaje = "Robot encendido. Ingrese distancia inicial."
                            elif robot.estado == 2:
                                running = False
                            else:
                                robot.mensaje = "Robot apagado"
                            input_text = ""
                            
                        elif current_mode == "distancia":
                            robot.distancia = float(input_text)
                            current_mode = None
                            input_prompt = "Robot en movimiento..."
                            robot.mensaje = f"Avanzando hacia obstáculo a {robot.distancia}m"
                            input_text = ""
                            
                        elif current_mode == "continuar":
                            robot.estado = int(input_text)
                            if robot.estado == 0:
                                robot.mensaje = "Apagando robot..."
                                pygame.display.flip()
                                time.sleep(1)
                                running = False
                            else:
                                current_mode = "direccion"
                                input_prompt = "Dirección (1=Izquierda, 0=Derecha):"
                                robot.mensaje = "Preparado para cambio de dirección"
                            input_text = ""
                            
                        elif current_mode == "direccion":
                            robot.girar(int(input_text))
                            current_mode = "distancia"
                            input_prompt = "Ingrese nueva distancia al obstáculo (metros):"
                            input_text = ""
                            
                    except ValueError:
                        robot.mensaje = "Error: Entrada no válida"
                        input_text = ""
                        
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_1 and current_mode == "estado":
                    input_text = "1"
                elif event.key == pygame.K_2 and current_mode == "estado":
                    input_text = "2"
                elif event.key == pygame.K_0 and current_mode in ["continuar", "direccion"]:
                    input_text = "0"
                elif event.key == pygame.K_1 and current_mode in ["direccion", "continuar"]:
                    input_text = "1"
                elif event.unicode.isdigit() or event.unicode == '.':
                    input_text += event.unicode
        
        # Lógica del simulador
        if robot.estado == 1 and current_mode is None:
            robot.actualizar_posicion()
            
            if robot.distancia <= 5:
                current_mode = "continuar"
                input_prompt = "Obstáculo detectado! Continuar? (1=Sí, 0=No):"
                robot.mensaje = f"Obstáculo cercano a {robot.distancia:.1f}m"
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()