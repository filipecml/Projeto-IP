import pygame
import os
import math

# Obtenha o caminho para a pasta "imagens" a partir do diretório atual
image_dir = os.path.join(os.path.dirname(__file__), 'imagens')

# Carregue a imagem diretamente usando o caminho completo
icon = pygame.image.load(os.path.join(image_dir, 'carblue.png'))

class RightCar:
    def __init__(self, x, y, x_change, largura):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.largura = largura
        self.image = pygame.image.load(os.path.join(image_dir, 'carblue.png'))  # Carregue a imagem no __init__

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        
    def drive(self):
        self.x += self.x_change

    def check_boundary(self):
        if self.x > self.largura + 70:  # Use 'self.largura' em vez de 'largura'
            self.x = -70

    def check_colisao(self, car_x, car_y, player_x, player_y):
        distance = math.sqrt((math.pow(player_x - car_x, 2) + math.pow(player_y - car_y, 2)))
        if distance < 27:
            return True
        
        else:
            return False


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
