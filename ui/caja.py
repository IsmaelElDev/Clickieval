import pygame

class Caja:
    def __init__(self,surface1,rect1,surface2,rect2,surface3,rect3,surface4,rect4):
        self.surface1 = surface1
        self.surface2 = surface2
        self.surface3 = surface3
        self.surface4 = surface4
        self.rect1 = rect1
        self.rect2 = rect2
        self.rect3 = rect3
        self.rect4 = rect4

    def draw(self,screen):
        screen.blit(self.surface1, (self.rect1.x, self.rect1.y))
        screen.blit(self.surface2, (self.rect2.x, self.rect2.y))
        screen.blit(self.surface3, (self.rect3.x, self.rect3.y))
        screen.blit(self.surface4, (self.rect4.x, self.rect4.y))

