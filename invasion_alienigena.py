import pygame
from pygame.sprite import Group

from configuraciones import Configuraciones

from nave import Nave

import funciones_juego as fj


def run_game():
    # Inicializar el juego , las configuraciones y crear objeto pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("Invasión_Alienígena")

    # Crea una nave
    nave = Nave(ai_configuraciones, pantalla)
    # Crea un grupo para almacenar las balas
    balas = Group()

    # Iniciar bucle principal del juego
    while True:

        # Escuchar eventos de teclado o ratón
        fj.verificar_eventos(ai_configuraciones, pantalla, nave, balas)
        nave.update()
        fj.update_balas(balas)
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave, balas)


run_game()
