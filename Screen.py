import pygame
import sys
import os

class Screen():
    
    def __init__(self):
        pygame.init()
        self.set_screen()
        self.get_mouse_pos()
    
    def set_screen(self):
        self.flags = pygame.SCALED | pygame.RESIZABLE 
        self.screen = pygame.display.set_mode(((800,800)), self.flags , vsync=1)
         
    def set_screen_color(self,col):
        self.screen.fill(col)


    def get_mouse_pos(self):
        self.mp = pygame.mouse.get_pos()
        self.mpx, self.mpy = self.mp[0], self.mp[1]
        

        

        

