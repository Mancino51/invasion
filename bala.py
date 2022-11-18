import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    """Sirve para manejar las balas disparadas desde la nave"""
    def __init__(self, ai_configuraciones, pantalla, nave):
        super(Bala, self).__init__()
        self.pantalla = pantalla

        # Crea una bala rect en (0, 0) y luego establece la posicion correcta
        self.rect = pygame.Rect(0, 0, ai_configuraciones.bala_width, ai_configuraciones.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        # Almacena la posicion de la bala como un valor decimal
        self.y = float(self.rect.y)

        self.color = ai_configuraciones.bala_color
        self.factor_velocidad = ai_configuraciones.bala_factor_velocidad

    def update(self):
        """Mueve la bala hacia arriba e la pantalla"""
        # Actualiza la posicion decimal de la bala
        self.y -= self.factor_velocidad
        # Actualiza la posicion del rect
        self.rect.y = self.y

    def draw_bala(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.pantalla, self.color, self.rect)
