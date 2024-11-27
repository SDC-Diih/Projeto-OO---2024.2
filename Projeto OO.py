import pygame
import random
import sys
from Screen import Screen
from Game import Game
from Prota import Prota
from Inimigos import Inimigos
from Button import Button

pygame.init()

#Título e Relógio
pygame.display.set_caption("Projeto OO")
clock = pygame.time.Clock()

#Mouse


screen_1 = Screen((1000,800))
jogo_1 = Game()
prota_1 = Prota(screen_1)
inimigos_1 = Inimigos(screen_1, prota_1)

button_1 = Button(screen_1.screen, "button.png", 400, 400, "Iniciar", scale = (500, 200))




#Tela Principal:
def Menu_principal():
    
    button_1.cena_jogo = False
    pygame.display.set_caption("Menu Principal")
    
    pygame.mouse.set_visible(True)
    jogo_1.set_run_true()
    while jogo_1.run:
        clock.tick(200)
        screen_1.set_screen_color("white")
        jogo_1.get_mouse_pos()
        
        
        button_1.create_and_function()
        
        jogo_1.event_get_keys()
        
        
        if button_1.cena_jogo == True:
            #screen_1.set_screen_color("black")
            jogo_1.set_run_false()
            jogo()
            
        pygame.display.update()  
        
    

#Jogo
def jogo():

    pygame.display.set_caption("Jogo")

    #Personagem Principal
    prota_1.prota_get_skin()
    prota_1.prota_get_pos()

    #Criação de Inimigos:
    inimigos_1.set_inimigos_spawn()
    inimigos_1.set_inimigos("red")
    
    
    jogo_1.cena_jogo = True
    while jogo_1.cena_jogo:
        clock.tick(200)
        screen_1.set_screen_color("#FfFf5f")
        screen_1.get_mouse_pos()
        pygame.mouse.set_visible(False)
        
        
        inimigos_1.set_speed_inimigos(2)
        
        #Sistema de Colisão
        inimigos_1.collision_check()
        
        #Prota movimentos
        prota_1.prota_get_controls()
        #jogo_1.event_get_keys()
        
        
                
        #Teste masks
        screen_1.screen.blit(prota_1.Prota_mask_imagem, (prota_1.pmi_x,prota_1.pmi_y))   
        screen_1.screen.blit(inimigos_1.Inimigo, (inimigos_1.ini_x, inimigos_1.ini_y)) 
                
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_ESCAPE:
                    jogo_1.cena_jogo = False
                    Menu_principal()
                    
        #Update screen
        pygame.display.update()  
    
#jogo()
Menu_principal()
