import pygame
from pygame.locals import *
from sys import exit
from obstaculos import lista_de_obstaculos
from personagem import Personagem

pygame.init()

largura = 1280
altura = 720

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CroCIn Road')

tamanho = 40
personagem = Personagem(largura/2 - tamanho/2, altura-75, tamanho, tela)  # Passe a tela como parâmetro

while True:
    # Desenhe o fundo da tela como grama (um retângulo verde-claro)
    tela.fill((34, 139, 34))  # Cor RGB para verde-claro

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Chame a função de processar eventos do personagem
    personagem.processar_eventos()

    # Desenhe o personagem
    personagem.criar_personagem()

    pygame.display.update()
