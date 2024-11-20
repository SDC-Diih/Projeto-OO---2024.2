import pygame
import sys
import os

class Game():
    def __init__(self):
        pass
        
    def event_get_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_ESCAPE:
                   self.run = False
        
    def set_run_true(self):
        self.run = True
    def set_run_false(self):
        self.run = False