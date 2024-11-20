import pygame
import sys

class Screen():
    
    def __init__(self):
        pygame.init()
        self.set_screen()
        self.set_default_colors()
    def set_default_colors(self):
        
        self.colors = {
        "Branco": (255, 255, 255),
        "Preto": (0, 0, 0),
        "Verde": (0, 255, 0),
        "Azul": (0, 0, 255),
        "Vermelho": (255, 0, 0),
        }
    
    def set_specific_colors(self, col):
        self.col = col
        return self.col
    def set_screen(self):
        self.flags = pygame.SCALED | pygame.RESIZABLE 
        self.screen = pygame.display.set_mode(((800,800)), self.flags , vsync=1)
         
    def set_screen_color(self,col):
        if col in self.colors:
            col = self.colors[col]
        else:
            pass
        self.screen.fill(col)

    def set_font(self, tipo, tamanho):
        return pygame.font.SysFont(name = tipo, size = tamanho)

    def button_text(self, font, text, tamanho, col, colrec):
        
        if col in self.colors:
            col = self.colors[col]
        else:
            pass
        
        # Desenhar texto no botão
        TEXT_BUTTON = self.set_font(font, tamanho).render(text, True, col)
        RET_BUTTON = TEXT_BUTTON.get_rect(center=(400, 200))
        pygame.draw.rect(self.screen, colrec , RET_BUTTON)
        self.screen.blit(TEXT_BUTTON, RET_BUTTON)  
        
    def get_mouse_pos(self):
        self.mp = pygame.mouse.get_pos()
        self.mpx, self.mpy = self.mp[0], self.mp[1]
        
class Game():
    def __init__(self):
        pygame.init()
        
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