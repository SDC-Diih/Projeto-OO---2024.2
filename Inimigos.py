import pygame
import sys
import os
import random
from Screen import Screen
screen_1 = Screen((1000,800))

class Inimigos():
    
    def __init__(self, screen_instance, prota_instance):
        
        self.screen = screen_instance.screen
        self.prota = prota_instance
        self.ini_x, self.ini_y = 0, 0
        self.Prota_mask = prota_instance.Prota_mask
        
         
    def set_inimigos(self, col):
        
        self.Inimigo = pygame.Surface((20, 20))
        self.Inimigo_mask = pygame.mask.from_surface(self.Inimigo)
        self.Inimigo_mask.to_surface() 
        self.Inimigo.fill(col)
        self.ini_x, self.ini_y = self.spawn_x, self.spawn_y
        self.screen.blit(self.Inimigo, (self.ini_x, self.ini_y))
            
    def set_speed_inimigos(self, ini_speed):
        
        self.ini_speed = ini_speed
        
        
        # Ponto central da tela
        mid_x, mid_y = screen_1.middle_point[0], screen_1.middle_point[1]
        
        
        # Distâncias do inimigo ao ponto central
        spd_mpx = self.ini_x - mid_x
        spd_mpy = self.ini_y - mid_y
        
        
        # Ajustar posição horizontalmente
        if spd_mpx > 5:
            self.ini_x -= self.ini_speed
        elif spd_mpx < -5:
            self.ini_x += self.ini_speed
        
        # Ajustar posição verticalmente
        if spd_mpy > 5:
            self.ini_y -= self.ini_speed
        elif spd_mpy < -5:
            self.ini_y += self.ini_speed
        
        
        #Verificar se está suficientemente próximo ao centro
        if ((-5 <= spd_mpy <= 5) and (-5 <= spd_mpx <= 5)):
            print("Chegou")
        else:
            pass
    def set_inimigos_spawn(self):
        self.spawn_x, self.spawn_y = random.randint(1, 1000), random.randint(0, 100)

    def collision_check(self):
        #self.mpx, self.mpy = pygame.mouse.get_pos()
        pmi_x, pmi_y = self.prota.pmi_x, self.prota.pmi_y
        
        if self.Prota_mask.overlap(self.Inimigo_mask, (self.ini_x - pmi_x,self.ini_y - pmi_y)):
            self.col = "blue"
        else:
            self.col = "red"
            
        self.Inimigo.fill(self.col)
        self.screen.blit(self.Inimigo, (self.ini_x, self.ini_y))