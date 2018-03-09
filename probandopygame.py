#
# probandopygame.py
#
# Descripcion: Programa que muestra el uso de la librería Pygame
#
# Autor:  Prep. Kevin Mena
#
# Ultima modificacion: 07/03/2018

import pygame
import os 

# CONSTANTES:
# Colores que seran usados en el juego
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Valores necesarias para la pantalla
ALTO = 720       # alto de la ventana
ANCHO = 1280     # ancho de la ventana
FPS = 30         # frames per second

# Variables:
#    pantalla: object    // para el manejo de la interfaz gráfica
#	 cuenta: object      // para el manejo del tiempo
#    evento: object      // para capturar los eventos producidos
#    jugando: bool       // dice si se continua en el juego

# Inicializar la pantalla del juego
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'                  # Centrar la ventana a la hora de abrirse
pantalla = pygame.display.set_mode((ANCHO, ALTO))       # Configurando la pantalla
pygame.display.set_caption("Mi juego")                  # Coloca titulo a nuestra pantalla
reloj = pygame.time.Clock()

# Loop del juego
jugando = True                                          

while jugando:
        # Como el juego es un loop todo su codigo va AQUI dentro

        # Hacer que el juego corrar a una velocidad que deseemos
        reloj.tick(FPS)

        # Se verifican los eventos que estan sucediendo
        ''' Siendo eventos definidos como sucesos que ocurren
        dependiendo de ciertas circunstancias (Ej: Tecla presionada)'''
        for evento in pygame.event.get():
            # Si el evento que esta ocurriendo es que se acabo el juego, entonces cerrarlo
            if evento.type == pygame.QUIT:
                jugando = False
            # Dibujar un circulo cuando se hace click con el mouse
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pantalla.fill(NEGRO)                    # Repinta la pantalla de negro
                pygame.draw.circle(pantalla, AZUL, evento.pos, 30, 0)

        # Cuadrado exterior
        pygame.draw.line(pantalla, VERDE, (130, 90), (130, 620))
        pygame.draw.line(pantalla, VERDE, (1120, 90), (1120, 620))
        pygame.draw.line(pantalla, VERDE, (130, 90), (1120, 90))
        pygame.draw.line(pantalla, VERDE, (130, 620), (1120, 620))

        # Filas
        pygame.draw.line(pantalla, VERDE, (130, 178), (1120, 178))
        pygame.draw.line(pantalla, VERDE, (130, 266), (1120, 266))
        pygame.draw.line(pantalla, VERDE, (130, 354), (1120, 354))
        pygame.draw.line(pantalla, VERDE, (130, 442), (1120, 442))
        pygame.draw.line(pantalla, VERDE, (130, 530), (1120, 530))

        # Columnas
        pygame.draw.line(pantalla, VERDE, (272, 90), (272, 620))
        pygame.draw.line(pantalla, VERDE, (414, 90), (414, 620))
        pygame.draw.line(pantalla, VERDE, (556, 90), (556, 620))
        pygame.draw.line(pantalla, VERDE, (698, 90), (698, 620))
        pygame.draw.line(pantalla, VERDE, (840, 90), (840, 620))
        pygame.draw.line(pantalla, VERDE, (982, 90), (982, 620))

        # DEBE IR DE ULTIMO
        # Funcion para mostrar en pantalla lo "pintado" luego de hacerlo
        pygame.display.flip()

# Cerrar el juego
pygame.quit()