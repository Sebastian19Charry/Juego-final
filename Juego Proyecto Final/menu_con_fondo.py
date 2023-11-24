import pygame
import subprocess
import sys

pygame.init()
pygame.display.set_caption("hero ritmico")

# Configuración de la pantalla
ancho_pantalla = 1066
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
fondo = pygame.image.load('fondo.jpg')
fondo = pygame.transform.scale(fondo, (ancho_pantalla, alto_pantalla))

# Configuración de los botones
ancho_boton = 200
alto_boton = 50
color_boton = (0, 255, 0)

# Crear los botones
boton_play = pygame.Rect(ancho_pantalla / 2 - ancho_boton / 2, alto_pantalla / 1.5 - alto_boton, ancho_boton, alto_boton)
boton_exit = pygame.Rect(ancho_pantalla / 2 - ancho_boton / 2, alto_pantalla / 1.5 + alto_boton, ancho_boton, alto_boton)

# Cargar las imágenes de los botones
imagen_boton_play = pygame.image.load('boton_play.png')
imagen_boton_play = pygame.transform.scale(imagen_boton_play, (ancho_boton, alto_boton))
imagen_boton_exit = pygame.image.load('boton_exit.png')
imagen_boton_exit = pygame.transform.scale(imagen_boton_exit, (ancho_boton, alto_boton))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_play.collidepoint(evento.pos):
                print("Botón Play presionado!")
                # Aquí se abre el archivo main.py usando subprocess
                subprocess.Popen(["python", "main.py"])

            if boton_exit.collidepoint(evento.pos):
                print("Botón Exit presionado!")
                sys.exit()

    pantalla.blit(fondo, (0, 0))

    # Dibujar los botones
    pygame.draw.rect(pantalla, color_boton, boton_play)
    pygame.draw.rect(pantalla, color_boton, boton_exit)
    pantalla.blit(imagen_boton_play, boton_play)
    pantalla.blit(imagen_boton_exit, boton_exit)
    pygame.display.flip()

pygame.quit()
