import pygame
import sys
import os



class Button():
    def __init__(self):
        pass
    
    

    def button_text(self, font, text, tamanho, col, colrec):
        
        if col in self.colors:
            col = self.colors[col]
        else:
            pass
        
        if colrec in self.colors:
            colrec = self.colors[colrec]
        else:
            pass
        
        # Desenhar texto no botão
        TEXT_BUTTON = self.set_font(font, tamanho).render(text, True, col)
        #Retângulo do butão + Coordenadas
        RET_BUTTON = TEXT_BUTTON.get_rect(center=(400, 200))
        pygame.draw.rect(self.screen, colrec , RET_BUTTON)
        self.screen.blit(TEXT_BUTTON, RET_BUTTON)  
        
        
        
        
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Button!")


class YtButton():

	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = self.main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):

		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

    def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.main_font.render(self.text_input, True, "green")
		else:
			self.text = self.main_font.render(self.text_input, True, "white")

    def set_font(self, tipo, tamanho):
        self.main_font = pygame.font.SysFont(name = tipo, size = tamanho)

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "assets", "button.png")
button_surface = pygame.image.load(image_path)
button_surface = pygame.transform.scale(button_surface, (400, 150))

button = YtButton(button_surface, 400, 300, "Button")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())

	screen.fill("white")

	button.update()
	button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()