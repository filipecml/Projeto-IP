import pygame
import os
from random import randint

image_dir = os.path.join(os.path.dirname(__file__), 'imagens')

class Coletavel:
        
        def __init__(self, image_filename, tela):
            self.x = randint(100, 500)
            self.y = randint(100, 650)
            self.tela = tela
            original_image = pygame.image.load(os.path.join(image_dir, image_filename))
            self.image = pygame.transform.scale(original_image, (50, 50))  # Redimensionar a imagem
            self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

        def draw(self, surface):
            surface.blit(self.image, (self.x, self.y))
            self.hitbox.topleft = (self.x, self.y)  # Atualizar a posição do hitbox

        def cria_coletavel(self):
            self.x = randint(100, 500)
            self.y = randint(100, 650)

        def processar_eventos(self):
            self.hitbox.x = self.x
            self.hitbox.y = self.y
        
        def check_colisao(self, player_hitbox):
            # Verifica a colisão usando o hitbox do jogador
            return self.hitbox.colliderect(player_hitbox)
