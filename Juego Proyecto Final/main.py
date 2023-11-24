import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la música
pygame.mixer.music.load('la groupie.mp3')  # Reemplaza con el nombre de tu archivo de música
pygame.mixer.music.play(-1)  # Reproducir la música en bucle

# Definir dimensiones de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Botones pulsadores y círculos")
fondo = pygame.image.load('fondo.png')

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Configuración del reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Variables para el control de generación de círculos
circle_radius = 15
circle_speed = 3.6  # Velocidad de descenso en píxeles por ciclo ajustada
spawn_rate = 8  # Número de círculos por segundo aumentado

# Estructura para controlar los tiempos de aparición de notas
note_timings = {
    0: [],
    1: [],
    2: [],
    3: [],
}

last_note_time = pygame.time.get_ticks()
next_note_time = 0  # Tiempo para la próxima generación de nota

# Función para generar círculos con un retraso aleatorio
def generate_circle(x, color):
    return {'x': x, 'y': 0, 'color': color}  # Empiezan desde la parte superior de la pantalla

circles = []

# Botones en forma de círculo en la parte inferior (ahora más grandes)
button_radius = 30  # Aumento del tamaño de los botones
button_spacing = 150  # Espacio entre los botones ajustado
buttons = [
    {'x': width // 5, 'y': height - 50, 'color': red, 'arrow': pygame.image.load('f_izquierda.png')},
    {'x': 2 * width // 5, 'y': height - 50, 'color': green, 'arrow': pygame.image.load('f_derecha.png')},
    {'x': 3 * width // 5, 'y': height - 50, 'color': blue, 'arrow': pygame.image.load('f_arriba.png')},
    {'x': 4 * width // 5, 'y': height - 50, 'color': yellow, 'arrow': pygame.image.load('f_abajo.png')},
]

# Escalar flechas para que coincidan con el tamaño de los botones
for button in buttons:
    button['arrow'] = pygame.transform.scale(button['arrow'], (60, 60))  # Ajuste del tamaño de las flechas

# Fuente para el puntaje
font = pygame.font.Font(None, 36)
score = 0

# Función para actualizar y mostrar el puntaje
def update_score():
    score_text = font.render(f"Puntaje: {score}", True, white)
    screen.blit(score_text, (20, 20))

# Bucle principal del juego
def main():
    global last_note_time
    global next_note_time
    global score

    while True:
        current_time = pygame.time.get_ticks()
        time_passed = current_time - last_note_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Movimiento controlado por las teclas de flecha y actualización de puntaje
        for i, button in enumerate(buttons):
            if keys[pygame.K_LEFT] and i == 0:
                if note_timings[i] and current_time - note_timings[i][-1] < 500:  
                    for circle in circles[::-1]:  # Verificar desde el último círculo hacia arriba
                        if circle['x'] == button['x'] and circle['y'] > height - 70:
                            score += 10
                            circles.remove(circle)
                            break
            elif keys[pygame.K_RIGHT] and i == 1:
                if note_timings[i] and current_time - note_timings[i][-1] < 500:
                    for circle in circles[::-1]:
                        if circle['x'] == button['x'] and circle['y'] > height - 70:
                            score += 10
                            circles.remove(circle)
                            break
            elif keys[pygame.K_UP] and i == 2:
                if note_timings[i] and current_time - note_timings[i][-1] < 500:
                    for circle in circles[::-1]:
                        if circle['x'] == button['x'] and circle['y'] > height - 70:
                            score += 10
                            circles.remove(circle)
                            break
            elif keys[pygame.K_DOWN] and i == 3:
                if note_timings[i] and current_time - note_timings[i][-1] < 500:
                    for circle in circles[::-1]:
                        if circle['x'] == button['x'] and circle['y'] > height - 70:
                            score += 10
                            circles.remove(circle)
                            break

        # Rellenar la pantalla con color negro
        screen.fill(black)

        # Dibujar líneas verticales blancas
        line_width = 5
        num_lines = 4
        line_spacing = width // (num_lines + 1)

        for i in range(1, num_lines + 1):
            x = i * line_spacing
            pygame.draw.line(screen, white, (x, 0), (x, height), line_width)

            # Controlar la generación de notas con tiempos específicos y aleatorios
            if time_passed > next_note_time and len(note_timings[i - 1]) < 5:
                if not note_timings[i - 1] or current_time - note_timings[i - 1][-1] > 3000:
                    note_timings[i - 1].append(current_time + random.randint(3000, 5000))
                    last_note_time = current_time
                    next_note_time = random.randint(1500, 3000)  # Retraso entre las siguientes notas ajustado

    
        # Actualizar y dibujar las notas
        for i, notes in enumerate(note_timings.values()):
            for note_time in notes[:]:
                if current_time > note_time:
                    note_timings[i].remove(note_time)
                    circles.append(generate_circle((i + 1) * line_spacing, buttons[i]['color']))
                    break  # Agrega un retraso entre las notas

        # Actualizar y dibujar los círculos
        for circle in circles[:]:
            pygame.draw.circle(screen, circle['color'], (circle['x'], circle['y']), circle_radius)
            circle['y'] += circle_speed

            # Eliminar círculos que llegan al borde inferior de la pantalla
            if circle['y'] > height:
                circles.remove(circle)

        # Dibujar botones en forma de círculo en la parte inferior
        for button in buttons:
            pygame.draw.circle(screen, button['color'], (button['x'], button['y']), button_radius)
            screen.blit(button['arrow'], (button['x'] - button['arrow'].get_width() // 2, button['y'] - 30))

        # Actualizar y mostrar el puntaje
        update_score()

        # Actualizar la pantalla
        pygame.display.flip()

        # Establecer la velocidad de fotogramas (FPS)
        clock.tick(60)  # Se ajusta a 60 FPS para una velocidad constante

if __name__ == "__main__":
    main()
