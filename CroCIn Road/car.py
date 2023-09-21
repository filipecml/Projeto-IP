import pygame
import os
import math
import random

# Obtenha o caminho para a pasta "imagens" a partir do diretório atual
image_dir = os.path.join(os.path.dirname(__file__), 'imagens')

# Carregue a imagem diretamente usando o caminho completo
icon = pygame.image.load(os.path.join(image_dir, 'carredright.png'))

class RightCar:
    def __init__(self, x, y, x_change, largura):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.largura = largura
        original_image = pygame.image.load(os.path.join(image_dir, 'carredright.png'))
        self.image = pygame.transform.scale(original_image, (80, 40))  # Redimensionar a imagem

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        
    def drive(self):
        self.x -= self.x_change

    def check_boundary(self):
        if self.x < -70:
            self.x = self.largura

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
        original_image = pygame.image.load(os.path.join(image_dir, 'carblue.png'))
        self.image = pygame.transform.scale(original_image, (80, 40))  # Redimensionar a imagem

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        
    def drive(self):
        self.x += self.x_change

    def check_boundary(self):
        if self.x > 600:
            self.x = -70

    def check_colisao(self, car_x, car_y, player_x, player_y):
        distance = math.sqrt((math.pow(player_x - car_x, 2) + math.pow(player_y - car_y, 2)))
        if distance < 27:
            return True
        else:
            return False
