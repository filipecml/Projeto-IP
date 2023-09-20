import pygame

class Cenario:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.grama_1 = pygame.image.load("C:\\Users\\kabes\\OneDrive\\Ambiente de Trabalho\\Faculdade.1\\CroCin Road\\Projeto-IP\\CroCIn Road\\imagens\\grama_1.png")
        self.grama_2 = pygame.image.load("C:\\Users\\kabes\\OneDrive\\Ambiente de Trabalho\\Faculdade.1\\CroCin Road\\Projeto-IP\\CroCIn Road\\imagens\\grama_2.png")
        self.grama_3 = pygame.image.load("C:\\Users\\kabes\\OneDrive\\Ambiente de Trabalho\\Faculdade.1\\CroCin Road\\Projeto-IP\\CroCIn Road\\imagens\\grama_3.png")
        self.rua = pygame.image.load("C:\\Users\\kabes\\OneDrive\\Ambiente de Trabalho\\Faculdade.1\\CroCin Road\\Projeto-IP\\CroCIn Road\\imagens\\rua_full.png")
        self.rio = pygame.image.load("C:\\Users\\kabes\\OneDrive\\Ambiente de Trabalho\\Faculdade.1\\CroCin Road\\Projeto-IP\\CroCIn Road\\imagens\\rio_full.png")
        self.linha_chegada = pygame.image.load("C:\\Users\\kabes\\OneDrive\\Ambiente de Trabalho\\Faculdade.1\\CroCin Road\\Projeto-IP\\CroCIn Road\\imagens\\chegada.png")

    def desenhar(self, tela):
        # Linha de chegada
        tela.blit(self.linha_chegada, (0, 0))
        # Grama 3
        tela.blit(self.grama_3, (0, self.linha_chegada.get_height()))
        # Rio
        tela.blit(self.rio, (0, self.linha_chegada.get_height() + self.grama_3.get_height()))
        # Grama 2
        tela.blit(self.grama_2, (0, self.linha_chegada.get_height() + self.grama_3.get_height() + self.rio.get_height()))
        # Rua
        tela.blit(self.rua, (0, self.linha_chegada.get_height() + self.grama_3.get_height() + self.rio.get_height() + self.grama_2.get_height()))
        # Grama 1
        tela.blit(self.grama_1, (0, self.linha_chegada.get_height() + self.grama_3.get_height() + self.rio.get_height() + self.grama_2.get_height() + self.rua.get_height()))