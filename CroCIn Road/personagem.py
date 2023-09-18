import pygame

class Personagem:
    def __init__(self, x, y, tamanho, tela):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.cor = (255, 255, 255)
        self.tela = tela
        self.velocidade = 1.5

    def criar_personagem(self):
        pygame.draw.rect(self.tela, self.cor, (self.x, self.y, self.tamanho, self.tamanho))

    def movimento(self, dx, dy):
        self.x += dx
        self.y += dy
