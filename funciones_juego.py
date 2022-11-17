import sys

import pygame
from bala import Bala

from alien import Alien



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


def actualizar_pantalla(ai_configutaciones, pantalla, nave, aliens,  balas):
    """Actualiza las imagenes en la pantalla y pasa a la nueva pantalla"""

    # Volver s dibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(ai_configutaciones.bg_color)
    # Vuelve a dibujar todas las balas detras de la nave y de los extraterestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    aliens.draw(pantalla)
    

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

def get_number_aliens_x(ai_configuraciones, alien_width):
    """" Determina el numero de aliens que caben en una fila """
    available_space_x = ai_configuraciones.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def crear_alien(ai_configuraciones, pantalla, aliens, alien_number):
    """Crea un alien y lo coloca en la fila"""
    alien = Alien(ai_configuraciones, pantalla)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien) 
    
        
def crear_flota(ai_configuraciones, pantalla, aliens):
    """Crea una flota completa de Aliens"""
    # Crea un Alien y encuentra el numero de Aliens seguidos
    # El espacio entre cada Alien es = a un ancho de Alien
    alien = Alien(ai_configuraciones, pantalla)
    number_aliens_x = get_number_aliens_x(ai_configuraciones, alien.rect.width)

    # Crea la primera fila de aliens
    for alien_number in range(number_aliens_x):
        crear_alien(ai_configuraciones, pantalla, alien_number)     
    
