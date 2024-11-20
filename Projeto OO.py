import pygame
import random
import sys
from Screen import Screen
from Game import Game
from Prota import Prota
from Inimigos import Inimigos
#from Button import YtButton

pygame.init()

#Título e Relógio
pygame.display.set_caption("Projeto OO")
clock = pygame.time.Clock()

#Mouse
pygame.mouse.set_cursor(pygame.cursors.diamond)
pygame.mouse.set_visible(True)

screen_1 = Screen()
jogo_1 = Game()
prota_1 = Prota(screen_1)
inimigos_1 = Inimigos(screen_1, prota_1)
#button_1 = YtButton(screen_1)

#Tela Principal:
def Menu_principal():
    
    pygame.display.set_caption("Menu Principal")
    
    jogo_1.set_run_true()
    while jogo_1.run:
        clock.tick(200)
        screen_1.set_screen_color("white")
        pygame.mouse.get_pos()
        
        #button_1.button_text(font = "arial",text = "ashjikdgashjkdgasukd", tamanho = 70, 
                             #col = "black", colrec = "#34dffd")
        
        jogo_1.event_get_keys()
                    
        pygame.display.update()  
        
    pygame.quit()
    

#Jogoasd
def jogo():

    #Personagem Principal
    prota_1.prota_get_skin()
    prota_1.prota_get_pos()

    #Criação de Inimigos:
    inimigos_1.set_inimigos("red")
    
    jogo_1.set_run_true()
    while jogo_1.run:
        clock.tick(200)
        screen_1.set_screen_color("#FfFf5f")
        screen_1.get_mouse_pos()
        pygame.mouse.set_visible(False)
        
        
        #Sistema de Colisão
        inimigos_1.collision_check()
        
        #Prota movimentos
        prota_1.prota_get_controls()
        jogo_1.event_get_keys()
        
        #Teste masks
        screen_1.screen.blit(prota_1.Prota_mask_imagem, (prota_1.pmi_x,prota_1.pmi_y))   
        screen_1.screen.blit(inimigos_1.Inimigo, screen_1.mp) 
                
        #Update screen
        pygame.display.update()  
    
jogo()
#Menu_principal()
