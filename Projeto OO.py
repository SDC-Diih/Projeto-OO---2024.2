import pygame
import random
import sys
from Buttons import Screen, Game

pygame.init()

#Título e Relógio
pygame.display.set_caption("Projeto OO")
clock = pygame.time.Clock()

#Mouse
pygame.mouse.set_cursor(pygame.cursors.diamond)
pygame.mouse.set_visible(True)

screen_1 = Screen()
jogo_1 = Game()

#Tela Principal:
def Menu_principal():
    
    pygame.display.set_caption("Menu Principal")
    
    jogo_1.set_run_true()
    while jogo_1.run:
        clock.tick(200)
        screen_1.set_screen_color("Branco")
        pygame.mouse.get_pos()
        
        screen_1.button_text(font = "arial",text = "ashjikdgashjkdgasukd", tamanho = 70, 
                             col = "Preto", colrec = "#34dffd")
        
        jogo_1.event_get_keys()
                    
        pygame.display.update()  
        
    pygame.quit()
    

#Jogo
def jogo():

    
    #Mouse/Personagem Principal
    Prota = pygame.image.load(r"C:\Users\diogo\Downloads\Prota3.png").convert_alpha()
    Prota_mask = pygame.mask.from_surface(Prota)
    Prota_mask_imagem = Prota_mask.to_surface()
    pmi_x = 0 
    pmi_y = 0


    #Criação de Inimigos:

    Inimigo = pygame.Surface((20, 20))
    Inimigo_mask = pygame.mask.from_surface(Inimigo)
        

    jogo_1.set_run_true()
    while jogo_1.run:
        clock.tick(200)
        screen_1.set_screen_color("#FfFf5f")
        screen_1.get_mouse_pos()
        pygame.mouse.set_visible(False)
        
        #Sistema de Colisão
        col = screen_1.colors["Vermelho"]
        if Prota_mask.overlap(Inimigo_mask, (screen_1.mpx - pmi_x,screen_1.mpy - pmi_y)):
            col = screen_1.colors["Azul"]
        
        #Objetos 
        
        Inimigo_mask.to_surface()
        Inimigo.fill(col)
        screen_1.screen.blit(Inimigo, (screen_1.mpx, screen_1.mpy))
        
        #Prota movimentos
        key = pygame.key.get_pressed()
        if key[pygame.K_w] == True:
            pmi_y -= 5
        if key[pygame.K_s] == True:
            pmi_y += 5
        if key[pygame.K_d] == True:
            pmi_x += 5
        if key[pygame.K_a] == True:
            pmi_x -= 5
            
        jogo_1.event_get_keys()
        
        #Teste masks
        
        screen_1.screen.blit(Prota_mask_imagem, (pmi_x,pmi_y))   
        screen_1.screen.blit(Inimigo, screen_1.mp) 
                
        #Update screen
        pygame.display.update()  
    
jogo()
#Menu_principal()
