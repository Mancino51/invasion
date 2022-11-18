import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Sirve para representar a u solo alieneigena en la flota"""
    def __init__(self, ai_configuraciones, pantalla):
        super(Alien,self).__init__()
        
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones
        
        # Carga la imagen del alien  y estable suatributo rec
        self.image = pygame.image.load("imagenes/alien.bmp")
        self.rect = self.image.get_rect()
        
        # Inicia cada nuevo alien cer de lapsrte superior  izq de lapantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Almacen la posicion exacta del alien
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Dibuja el alien en su ubicacion actual"""
        self.pantalla.blit(self.imagen, self.rect)
        
    def check_edges(self):
        """Devueve verdadro si el alien está en el borde de la pantalla"""
        screen_rect = self.pantalla.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
        
    def update(self):
        """ mueve el alien a la derecha"""
        self.x += (self.ai_configuraciones.alien_speed_factor * self.ai_configuraciones.fleet_direction)
        self.rect.x = self.x
        
        

