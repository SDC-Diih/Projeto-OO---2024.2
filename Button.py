import pygame
import sys
import os
from Game import Game


pygame.init()
class Button(Game):
	def __init__(self,screen, image, x_pos, y_pos, text_input, scale):
     
		super(Button, self).__init__
  
		self.cena_jogo = False
  
		self.scale = scale
		self.screen = screen
		self.image = image
		#Coordenadas do botão na tela
		self.x_pos = x_pos
		self.y_pos = y_pos
  
		#Criação do texto e retângulo das coordenadas do botão
		self.text_input = text_input
		self.main_font = pygame.font.SysFont("arial", 70)
		self.text = self.main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

		self.set_image(image, scale)	
		
 
	def create_and_function(self):
		#Atualiza a posição do botão e do texto com as coordenadas dos seus retângulos
		self.screen.blit(self.button_surface, self.rect)
		self.screen.blit(self.text, self.text_rect)
  
		#Realiza os comandos necessários para a checagem das operações do botão

	
		self.get_mouse_pos()
		self.checkForInput(self.mouse_position)
		self.changeColor(self.mouse_position)
  
	def checkForInput(self, position):
		#Checar posição do mouse
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			for event in pygame.event.get():
				#Checar click do mouse no botão
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.cena_jogo = True
					
					
        
        
	def changeColor(self, position):
		#Checar posição do mouse
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			#Trocar a cor para Verde caso o mouse esteja sobre o botão
			self.text = self.main_font.render(self.text_input, True, "green")
		else:
			#Manter a cor do botão - No caso Branca
			self.text = self.main_font.render(self.text_input, True, "white")


	def set_font(self, tipo, tamanho):
		#Selecionar a fonte do texto do botão
		self.main_font = pygame.font.SysFont(name = tipo, size = tamanho)


	def set_image(self, image, scale):
		#Escolher a imagem do fundo do botão + Colocar ele em escala se necessário
		self.current_dir = os.path.dirname(__file__)
		self.image_path = os.path.join(self.current_dir, "assets", image)
		self.button_surface = pygame.image.load(self.image_path)
		#Checa se a escala está em tupla -> (xxx,yyy) / Se não estiver não faz nada
		if isinstance(scale, tuple):
			self.button_surface = pygame.transform.scale(self.button_surface, scale)
		self.rect = self.button_surface.get_rect(center=(self.x_pos, self.y_pos))



