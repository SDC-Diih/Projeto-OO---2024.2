import pygame
import sys
import os

class Screen():
    
    def __init__(self, size):
        self.size = size
        pygame.init()
        self.set_screen(self.size)
        self.get_mouse_pos()
        self.get_screen_middle_point(size)
    def set_screen(self, size):
        self.flags = pygame.SCALED | pygame.RESIZABLE 
        self.screen = pygame.display.set_mode(size, self.flags , vsync=1)
         
    def set_screen_color(self,col):
        self.screen.fill(col)


    def get_mouse_pos(self):
        self.mp = pygame.mouse.get_pos()
        self.mpx, self.mpy = self.mp[0], self.mp[1]
        
    def get_screen_middle_point(self, size):
        self.middle_point = (self.size[0]/2, self.size[1]/2)

        

        

