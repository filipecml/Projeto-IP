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
        self.image = pygame.transform.scale(original_image, (100, 80))  # Redimensionar a imagem
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.hitbox.topleft = (self.x, self.y)  # Atualizar a posição do hitbox

    def drive(self):
        self.x -= self.x_change
        self.hitbox.topleft = (self.x, self.y)  # Atualizar a posição do hitbox

    def check_boundary(self):
        if self.x < -70:
            self.x = self.largura

    def check_colisao(self, player_hitbox):

        # Verifique a colisão usando o hitbox do jogador
        return self.hitbox.colliderect(player_hitbox)

   
class LeftCar:
    def __init__(self, x, y, x_change, largura):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.largura = largura
        original_image = pygame.image.load(os.path.join(image_dir, 'carblue.png'))
        self.image = pygame.transform.scale(original_image, (100, 50))  # Redimensionar a imagem
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.hitbox.topleft = (self.x, self.y)  # Atualizar a posição do hitbox

    def drive(self):
        self.x += self.x_change
        self.hitbox.topleft = (self.x, self.y)  # Atualizar a posição do hitbox

    def check_boundary(self):
        if self.x > 600:
            self.x = -70

    def check_colisao(self, player_hitbox):

        # Verifique a colisão usando o hitbox do jogador
        return self.hitbox.colliderect(player_hitbox)