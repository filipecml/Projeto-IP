import pygame
import os

# Obtenha o caminho para a pasta "imagens" a partir do diretório atual
image_dir = os.path.join(os.path.dirname(__file__), 'imagens')

# Carregue a imagem diretamente usando o caminho completo
icon = pygame.image.load(os.path.join(image_dir, 'carblue.png'))

class RightCar:
    def __init__(self, x, y, x_change, largura):  # Adicione 'largura' como argumento
        self.x = x
        self.y = y
        self.x_change = x_change
        self.largura = largura  # Armazene a largura como um atributo da classe
    
    def draw(self, surface):
        img = pygame.image.load(os.path.join(image_dir, 'carblue.png'))
        surface.blit(img, (self.x, self.y))
        
    def drive(self):
        self.x += self.x_change

    def check_boundary(self):
        if self.x > self.largura + 70:  # Use 'self.largura' em vez de 'largura'
            self.x = -70



class LeftCar:
    def __init__(self, x, y, x_change):
        self.x = x
        self.y = y
        self.x_change = x_change
    
    def draw(self, surface):
        pass

    def drive(self):
        pass

    def check_boundary(self):
        pass
