import pygame

class MejoraTarjeta:
    def __init__(self, nombre, pos, font_titulo, font_texto):
        self.nombre = nombre
        self.original_y = pos[1]
        self.rect = pygame.Rect(pos[0], pos[1], 300, 85)
        self.font_titulo = font_titulo
        self.font_texto = font_texto
        self.hover_color = (200, 200, 100)
        self.normal_color = (120, 120, 120)
        self.current_color = self.normal_color

    def draw(self, surface, cantidad, imagen, texto_nombre, texto_coste, scroll_y=0):
        # Crear un nuevo rect ajustado por scroll_y para el dibujo
        draw_rect = pygame.Rect(self.rect.x, self.rect.y - scroll_y, self.rect.width, self.rect.height)
        pygame.draw.rect(surface, self.current_color, draw_rect)
        surface.blit(imagen, (draw_rect.x + 10, draw_rect.y + 10))
        surface.blit(texto_nombre, (draw_rect.x + 100, draw_rect.y + 10))
        surface.blit(texto_coste, (draw_rect.x + 100, draw_rect.y + 40))

    def collidepoint(self, pos, scroll_y):
        # Ajustamos la posición Y del rect con scroll_y para comparar con las coordenadas del mouse
        # El mouse está en coordenadas de pantalla (relativas a upgrade_list_rect)
        # Pero el rect de la tarjeta necesita ajustarse hacia arriba por scroll_y
        check_rect = pygame.Rect(
            self.rect.x, 
            self.rect.y - scroll_y,  # Ajustar por scroll
            self.rect.width, 
            self.rect.height
        )
        return check_rect.collidepoint(pos)