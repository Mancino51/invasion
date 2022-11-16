class Configuraciones(object):
    """Sirve para almacenar todas las configuraciones de Invasión Alienígena"""

    def __init__(self):
        """Inicializar las configuraciones del  juego"""

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Configuraciones de la nave
        self.factor_velocidad_nave = 1.5

        # Configuraciones de balas
        self.bala_factor_velocidad = 1
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = 60, 60, 60
        self.balas_allowed = 3
