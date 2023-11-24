import pygame
import sys
import os

# Inicializar Pygame
pygame.init()

# Configuración de la ventana del menú
window_size = (800, 600)  # Puedes ajustar el tamaño de la ventana
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Menú')
fondo = pygame.image.load('fondo.jpg')
# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fuente para el texto
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        window.fill(WHITE)

        # Dibujar los botones
        play_button = pygame.Rect(300, 250, 200, 50)
        quit_button = pygame.Rect(300, 350, 200, 50)

        pygame.draw.rect(window, RED, play_button)
        draw_text('Jugar', font, WHITE, window, 345, 260)

        pygame.draw.rect(window, RED, quit_button)
        draw_text('Salir', font, WHITE, window, 350, 360)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if play_button.collidepoint(mouse_pos):
                        # Llamar al archivo principal del juego al presionar "Jugar"
                        os.system("python main.py")  # Esto ejecutará main.py

                    if quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

        pygame.display.update()
            
if __name__ == "__main__":
    main_menu()
