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

def get_number_rows(ai_configuraciones, nave_height, alien_height):
    """Determina el numero de filas de alien que se ajustan a la pantalla"""
    available_space_y = (ai_configuraciones.screen_height - (3 * alien_height) - nave_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def crear_alien(ai_configuraciones, pantalla, aliens, alien_number,row_number):
    """Crea un alien y lo coloca en la fila"""
    alien = Alien(ai_configuraciones, pantalla)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien) 
    
    
def crear_flota(ai_configuraciones, pantalla, nave, aliens):
    """Crea una flota completa de Aliens"""
    # Crea un Alien y encuentra el numero de Aliens seguidos
    # El espacio entre cada Alien es = a un ancho de Alien
    alien = Alien(ai_configuraciones, pantalla)
    number_aliens_x = get_number_aliens_x(ai_configuraciones, alien.rect.width)
    number_rows = get_number_rows(ai_configuraciones, nave.rect.height, alien.rect.height)
    

    # Crea la flota  de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            crear_alien(ai_configuraciones, pantalla, aliens, alien_number, row_number)   

def check_fleet_edges(ai_configuraciones, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_configuraciones, aliens)
            break
        
def change_fleet_direction(ai_configuraciones, aliens):
    """desciente toda la flota y cambia la direcion de la flota"""
    for alien in aliens.sprites():
        alien.rect.y += ai_configuraciones.fleet_drop_speed
        ai_configuraciones.fleet_direction *= -1
        
def update_aliens(ai_configuraciones, aliens):
    """Comprueba si la flota esta al borde y luego actualiza las posiciones de todos los aliens de la flota"""
    check_fleet_edges(ai_configuraciones, aliens)
    aliens.update()
    