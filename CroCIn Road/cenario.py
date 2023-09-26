import pygame
import os

class Cenario:
    def __init__(self, largura, altura):
        self.current_dir = os.path.dirname(__file__)
        
        self.largura = largura
        self.altura = altura
        self.grama_0 = pygame.image.load(os.path.join(self.current_dir, "imagens", "grama_0.png"))
        self.grama_1 = pygame.image.load(os.path.join(self.current_dir, "imagens", "grama_1.png"))
        self.grama_2 = pygame.image.load(os.path.join(self.current_dir, "imagens", "grama_2.png"))
        self.grama_3 = pygame.image.load(os.path.join(self.current_dir, "imagens", "grama_3.png"))
        self.rua = pygame.image.load(os.path.join(self.current_dir, "imagens", "rua_full.png"))
        self.linha_chegada = pygame.image.load(os.path.join(self.current_dir, "imagens", "chegada.png"))

    def desenhar(self, tela):
        # Linha de chegada
        tela.blit(self.linha_chegada, (0, 0))
        # Grama 3
        tela.blit(self.grama_3, (0, self.linha_chegada.get_height()))
        # Rua
        tela.blit(self.rua, (0, self.linha_chegada.get_height() + self.grama_3.get_height()))
        # Grama 2
        tela.blit(self.grama_2, (0, self.linha_chegada.get_height() + self.grama_3.get_height() + self.rua.get_height()))
        # Rua
        tela.blit(self.rua, (0, self.linha_chegada.get_height() + self.grama_3.get_height() + self.rua.get_height() + self.grama_2.get_height()))
        # Grama 1
        tela.blit(self.grama_1, (0, self.linha_chegada.get_height() + self.grama_3.get_height() + self.rua.get_height() + self.grama_2.get_height() + self.rua.get_height()))
        # Grama 0
        tela.blit(self.grama_0, (0, self.linha_chegada.get_height() + self.grama_3.get_height() + self.rua.get_height() + self.grama_2.get_height() + self.rua.get_height() + self.grama_0.get_height()))
