import pygame
import sys
import os
from Screen import Screen
screen_1 = Screen

class Game():
    def __init__(self):
        pass
        
    def event_get_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        
    def set_run_true(self):
        self.run = True
    def set_run_false(self):
        self.run = False
        
        
    def cena_jogo_true(self):
        self.cena_jogo = True
        
    def cena_jogo_false(self):
        self.cena_jogo = False
    
    def get_mouse_pos(self):
        self.mouse_position = pygame.mouse.get_pos()