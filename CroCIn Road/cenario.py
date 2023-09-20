import pygame

class Cenario:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.grama_1 = pygame.image.load("grama_1.png")
        self.grama_2 = pygame.image.load("grama_2.png")
        self.grama_3 = pygame.image.load("grama_3.png")
        self.rua = pygame.image.load("rua_full.png")
        self.rio = pygame.image.load("rio_full.png")
        self.linha_chegada = pygame.image.load("chegada.png")

    def desenhar(self, tela):
        # Linha de chegada
        tela.blit(self.linha_chegada, (self.largura - self.linha_chegada.get_width(), 0))
        # 3ª grama
        tela.blit(self.grama_3, (self.largura - self.grama_3.get_width(), self.altura - self.grama_3.get_height()))
        # Rio
        tela.blit(self.rio, (self.largura - self.grama_3.get_width() - self.rio.get_width(), self.altura - self.rio.get_height()))
        # 2ª grama
        tela.blit(self.grama_2, (self.largura - self.grama_3.get_width() - self.rio.get_width() - self.grama_2.get_width(), self.altura - self.grama_2.get_height()))
        # Rua
        tela.blit(self.rua, (self.largura - self.grama_3.get_width() - self.rio.get_width() - self.grama_2.get_width() - self.rua.get_width(), self.altura - self.rua.get_height()))
        # 1ª grama
        tela.blit(self.grama_1, (self.largura - self.grama_3.get_width() - self.rio.get_width() - self.grama_2.get_width() - self.rua.get_width() - self.grama_1.get_width(), self.altura - self.grama_1.get_height()))