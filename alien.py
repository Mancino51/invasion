import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Sirve para representar a u solo alieneigena en la flota"""
    def __init__(self, ai_configuraciones, pantalla):
        super(Alien,self).__init__()
        
        self.pantalla = pantalla
        self.ai_configuaciones = ai_configuraciones
        
        # Carga la imagen del alien  y estable suatributo rec
        self.image = pygame.image.load("imagenes/alien.bmp")
        self.rect = self.image.get_rect()
        
        # Inicia cada nuevo alien cer de lapsrte superior izq de lapantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Almacen la posicion exacta del alien
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Dibuja el alien en su ubicacion actual"""
        self.pantalla.blit(self.imagen, self.rect)
        

