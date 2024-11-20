import pygame
import sys
import os
from Screen import Screen

class Inimigos():
    
    def __init__(self, screen_instance, prota_instance):
        self.screen = screen_instance.screen
        
        self.prota = prota_instance
        self.mpx, self.mpy = 0, 0
        self.Prota_mask = prota_instance.Prota_mask
        
         
    def set_inimigos(self, col):
        
        self.Inimigo = pygame.Surface((20, 20))
        self.Inimigo_mask = pygame.mask.from_surface(self.Inimigo)
        self.Inimigo_mask.to_surface()
        self.Inimigo.fill(col)
        self.screen.blit(self.Inimigo, (self.mpx, self.mpy))
    
        

    def collision_check(self):
        self.mpx, self.mpy = pygame.mouse.get_pos()
        pmi_x, pmi_y = self.prota.pmi_x, self.prota.pmi_y
        
        if self.Prota_mask.overlap(self.Inimigo_mask, (self.mpx - pmi_x,self.mpy - pmi_y)):
            self.col = "blue"
        else:
            self.col = "red"
            
        self.Inimigo.fill(self.col)
        self.screen.blit(self.Inimigo, (self.mpx, self.mpy))