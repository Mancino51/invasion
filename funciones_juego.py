import sys

import pygame
from bala import Bala


def verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas):
    """Responde a las pulsaciones de las teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        fuego_bala(ai_configuraciones, pantalla, nave, balas)
    elif event.key == pygame.K_q:
        sys.exit()


def verificar_eventos_keyup(event, nave):
    """Responde a las pulsaciones de teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False


def verificar_eventos(ai_configuraciones, pantalla, nave, balas):
    """Responde a las pulsaciones de tecla y los eventos del raton"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas)

        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)


def actualizar_pantalla(ai_configutaciones, pantalla, nave,alien,  balas):
    """Actualiza las imagenes en la pantalla y pasa a la nueva pantalla"""

    # Volver s dibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(ai_configutaciones.bg_color)
    # Vuelve a dibujar todas las balas detras de la nave y de los extraterestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    alien.blitme()
    

    # Hacer visible la pantalla dibujasa mas reciente
    pygame.display.flip()


def update_balas(balas):
    """Actualiza la posicion de las balas y elimna las antiguas"""
    # Actualiza las posiciones de las balas
    balas.update()
    

    # Deshace las balas que han desaparecido
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

def fuego_bala(ai_configuraciones, pantalla, nave, balas):
    """Dispara una bala si aun no ha alcanzado el limite"""
    # Crea una nueva bala y la agrega al grupo de balas
    if len(balas) < ai_configuraciones.balas_allowed:
        nueva_bala = Bala(ai_configuraciones, pantalla, nave)
        balas.add(nueva_bala)
