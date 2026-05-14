# importamos la libreria pygame
import pygame
import sys

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((600,600))

# establecer titulo de la ventana
pygame.display.set_caption("trencito del capitan topa ;)")

# definición colores
negro = (0, 0, 0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255, 165, 0)
amarillo = (255, 255, 0)
fusia = (255, 0, 255)
verde = (0, 255, 0)
blanco = (255, 255, 255)
cian = (0, 255, 255)
morado = (128, 0, 128)
cafe = (139, 69, 19)
gris = (128, 128, 128)
cafe_claro = (205, 133, 63)
rosa = (255, 192, 203)
# variable de movimiento
XX = 300
MOVIMIENTO = 3

# Objeto para la gestión del tiempo
clock = pygame.time.Clock()


# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul, (0,0, 600, 400))
    ventana.fill(verde, (0, 400, 600, 200))

    # movimiento del rectángulo
    XX = XX + MOVIMIENTO

    if XX >= 485:
        XX = 485
        MOVIMIENTO = -1
    elif XX <= -115:
        XX = 600
        MOVIMIENTO = 1
    XX = XX + MOVIMIENTO


    # dibujar trensito
    pygame.draw.rect(ventana, gris, (XX,300,115,80))
    pygame.draw.circle(ventana, gris, (XX + 20, 380), 15)
    pygame.draw.circle(ventana, gris, (XX + 105, 380), 15)
    pygame.draw.circle(ventana, gris, (XX + 62.5, 380), 15)
    pygame.draw.rect(ventana, negro, (XX + 20,380,90,7))
    pygame.draw.rect(ventana, negro, (XX + 50,255,55,45))
    pygame.draw.rect(ventana, gris, (XX + 45,245,63,15))
    pygame.draw.rect(ventana, gris, (XX + 59,235,50,15))
    pygame.draw.rect(ventana, blanco, (XX + 57,260,42,25))
    pygame.draw.rect(ventana, blanco, (XX + -16, 307, 17,67))




    fuente_aria = pygame.font.SysFont("arial", 35, 1, 1)
    texto = fuente_aria.render("Daniel Felipe", 1, amarillo)
    ventana.blit(texto, (0,50))

    pygame.display.flip()