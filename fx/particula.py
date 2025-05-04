import pygame
import random

class Particula:
    def __init__(self, pos, vel,imagen, alpha=255, tiempo_vida=30):
        self.pos = list(pos)              # [x, y]
        self.vel = list(vel)              # [vx, vy]
        self.alpha = alpha          # Transparencia (0-255)
        self.tiempo_vida = tiempo_vida
        self.imagen = imagen
        self.imagen = pygame.transform.scale(self.imagen, (16, 16))

    def actualizar(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.vel[1] += 0.8  # gravedad
        self.tiempo_vida -= 1
        self.alpha -= 8
        if self.alpha < 0:
            self.alpha = 0

    def dibujar(self, screen):
        temp_imagen = self.imagen.copy()
        temp_imagen.set_alpha(self.alpha)
        screen.blit(temp_imagen, self.pos)

    def ha_muerto(self):
        return self.tiempo_vida <= 0
