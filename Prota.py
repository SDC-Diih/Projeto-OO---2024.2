import pygame
import sys
import os

class Prota():
    
    def __init__(self, screen_instance):
        self.screen = screen_instance.screen

        self.prota_get_pos()
        self.prota_get_skin()
    def prota_get_skin(self):
        #Personagem Principal
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "assets", "Prota3.png")
        self.Prota = pygame.image.load(image_path).convert_alpha()
        self.Prota_mask = pygame.mask.from_surface(self.Prota)
        self.Prota_mask_imagem = self.Prota_mask.to_surface()
        
    def prota_update(self):
        #Teste masks
        self.screen.blit(self.Prota_mask_imagem, (self.pmi_x,self.pmi_y)) 
        
    def prota_get_pos(self):
        self.pmi_x = 400
        self.pmi_y = 400
    def prota_get_controls(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] == True:
            self.pmi_y -= 5
        if key[pygame.K_s] == True:
            self.pmi_y += 5
        if key[pygame.K_d] == True:
            self.pmi_x += 5
        if key[pygame.K_a] == True:
            self.pmi_x -= 5
        