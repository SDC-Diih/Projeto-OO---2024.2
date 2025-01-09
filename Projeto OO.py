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


#Classes
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
        
        #Update Screen
        pygame.display.update()  
        

#Jogo
def jogo():

    pygame.display.set_caption("Jogo")

    #Personagem Principal
    prota_1.prota_get_skin()
    prota_1.prota_get_pos()

    #Criação de Inimigos:
    
    inimigos_1.set_inimigos(col = "red",quantidade = 20)
        
    jogo_1.cena_jogo = True
    while jogo_1.cena_jogo:
        clock.tick(200)
        screen_1.set_screen_color("#FfFf5f")
        screen_1.get_mouse_pos()
        pygame.mouse.set_visible(False)
        
        prota_1.prota_update()
        
        
        
        #Movimentar + Deletar e Criar caso esteja no fim da tela
        inimigos_1.movimentar_inimigos()
        inimigos_1.deletar_criar()
        
        #Detecção de Colisão
        inimigos_1.collision_check()
        
        #Prota movimentos
        prota_1.prota_get_controls()
        #jogo_1.event_get_keys()
        
        
                
          
                
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_ESCAPE:
                    jogo_1.cena_jogo = False
                    Menu_principal()
                    
        #Update screen
        pygame.display.update() 
    
Menu_principal()   
#jogo()
pygame.quit()
sys.exit()
