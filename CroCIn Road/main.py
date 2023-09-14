import pygame
from pygame.locals import *
from sys import exit
from obstaculos import lista_de_obstaculos

pygame.init()

largura = 1500
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CroCIn Road')

while True:
    # Desenhe o fundo da tela como grama (um retângulo verde-claro)
    tela.fill((34, 139, 34))  # Cor RGB para verde-claro

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Atualize e desenhe os obstáculos dentro do loop principal
    lista_de_obstaculos.update()
    lista_de_obstaculos.draw(tela)

    pygame.display.update()
