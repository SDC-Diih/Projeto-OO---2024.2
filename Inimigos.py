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
        self.inimigos = []  # Lista para armazenar os inimigos
         
    def set_inimigos(self, col, quantidade):
        self.quantidade = quantidade
        #Cria múltiplos inimigos e os armazena na lista
        for i in range(quantidade):
            # Criação de cada inimigo
            inimigo = {
                'surface': pygame.Surface((20, 20)),
                'mask': pygame.mask.from_surface(pygame.Surface((20, 20))),
                'x': random.randint(0, 0),
                'y': random.randint(0, 0),
                'speed': 1  # Velocidade inicial
            }
            inimigo['surface'].fill(col)
            inimigo['mask'] = pygame.mask.from_surface(inimigo['surface'])
            
            self.inimigos.append(inimigo)
            
    def set_speed_inimigos(self, ini_speed):
        
        for inimigo in self.inimigos:
            inimigo['speed'] = ini_speed
        
    def movimentar_inimigos(self):
        # Ponto central da tela
        self.mid_x, self.mid_y = self.screen.get_width() // 2, self.screen.get_height() // 2
        
        
        
        for inimigo in self.inimigos:
            # Distâncias do inimigo ao ponto central
            self.spd_mpx = inimigo['x'] - self.mid_x
            self.spd_mpy = inimigo['y'] - self.mid_y
            
            # Ajustar posição horizontalmente
            if self.spd_mpx > 5:
                inimigo['x'] -= inimigo['speed']
            elif self.spd_mpx < -5:
                inimigo['x'] += inimigo['speed']
            
            # Ajustar posição verticalmente
            if self.spd_mpy > 5:
                inimigo['y'] -= inimigo['speed']
            elif self.spd_mpy < -5:
                inimigo['y'] += inimigo['speed']
    def deletar_criar(self):
        #Verificar se está suficientemente próximo ao centro e DELETAR quando estiver
        
        novos_inimigos = []
        
        for i in range(len(self.inimigos)):
            inimigo = self.inimigos[i]
            
            # Verificar se o inimigo está suficientemente próximo do centro
            self.spd_mpx = inimigo['x'] - self.mid_x
            self.spd_mpy = inimigo['y'] - self.mid_y
            
            if ((-5 <= self.spd_mpy <= 5) and (-5 <= self.spd_mpx <= 5)):
                
                 # Quando o inimigo atinge o centro, remove o inimigo atual
                self.inimigos.pop(i)
                
                # Cria um novo inimigo 
                self.set_inimigos(col="red", quantidade=1)
                # Importante: Depois de remover o inimigo, deve-se interromper esse ciclo
                # A operação de pop altera o tamanho da lista, então interrompemos o loop para reiniciar a iteração
                
                
                break
        
    def set_inimigos_spawn(self):
        for inimigo in self.inimigos:
            self.lado = random.randint(1,4)
    
            if self.lado == 1:
                #Cima 
                inimigo['x'] = random.randint(0, self.screen.get_width())
                inimigo['y'] = random.randint(0, self.screen.get_width()//15)
            if self.lado == 2:
                #Baixo
                inimigo['x'] = random.randint(0, self.screen.get_width())
                inimigo['y'] = random.randint(self.screen.get_height()//15, self.screen.get_height())
            if self.lado == 3:
                #Esquerda 
                inimigo['x'] = random.randint(0, self.screen.get_width()//15)
                inimigo['y'] = random.randint(0, self.screen.get_height())
            if self.lado == 4:
                #Direita
                inimigo['x'] = random.randint(self.screen.get_height()//15, self.screen.get_height())
                inimigo['y'] = random.randint(0, self.screen.get_height())

    def collision_check(self):
        #self.mpx, self.mpy = pygame.mouse.get_pos()
        pmi_x, pmi_y = self.prota.pmi_x, self.prota.pmi_y
        
        for inimigo in self.inimigos:
            if self.Prota_mask.overlap(inimigo['mask'], (inimigo['x'] - pmi_x, inimigo['y'] - pmi_y)):
                col = "blue"
            else:
                col = "red"
            
            inimigo['surface'].fill(col)
            self.screen.blit(inimigo['surface'], (inimigo['x'], inimigo['y']))