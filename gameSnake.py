import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Snake Game')

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()
velocidad = 15

# Tamaño de los bloques de la serpiente y la comida
tamano_bloque = 20

# Fuente para mostrar el puntaje
fuente_puntaje = pygame.font.SysFont("comicsansms", 35)

def mostrar_puntaje(puntaje):
    valor = fuente_puntaje.render("Tu Puntaje: " + str(puntaje), True, blanco)
    pantalla.blit(valor, [0, 0])

def nuestra_serpiente(tamano_bloque, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(pantalla, verde, [x[0], x[1], tamano_bloque, tamano_bloque])

def gameLoop():
    game_over = False
    game_cerrado = False

    x1 = ancho_pantalla / 2
    y1 = alto_pantalla / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_serpiente = []
    largo_serpiente = 1

    comida_x = round(random.randrange(0, ancho_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque
    comida_y = round(random.randrange(0, alto_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque

    while not game_over:

        while game_cerrado == True:
            pantalla.fill(negro)
            mensaje_final = fuente_puntaje.render("¡Perdiste! Presiona Q para Salir o C para Jugar de Nuevo", True, rojo)
            pantalla.blit(mensaje_final, [ancho_pantalla / 6, alto_pantalla / 3])
            mostrar_puntaje(largo_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_cerrado = False
                    if evento.key == pygame.K_c:
                        gameLoop()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamano_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamano_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamano_bloque
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamano_bloque
                    x1_cambio = 0

        if x1 >= ancho_pantalla or x1 < 0 or y1 >= alto_pantalla or y1 < 0:
            game_cerrado = True
        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(negro)
        pygame.draw.rect(pantalla, azul, [comida_x, comida_y, tamano_bloque, tamano_bloque])
        lista_cabeza = []
        lista_cabeza.append(x1)
        lista_cabeza.append(y1)
        lista_serpiente.append(lista_cabeza)
        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        for x in lista_serpiente[:-1]:
            if x == lista_cabeza:
                game_cerrado = True

        nuestra_serpiente(tamano_bloque, lista_serpiente)
        mostrar_puntaje(largo_serpiente - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque
            comida_y = round(random.randrange(0, alto_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque
            largo_serpiente += 1

        reloj.tick(velocidad)

    pygame.quit()
    quit()

gameLoop()
