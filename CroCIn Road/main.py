import pygame
from pygame.locals import *
from sys import exit
from obstaculos import lista_de_obstaculos

pygame.init()

largura = 1500
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CroCIn Road')

# Cor de fundo verde mais escuro (por exemplo, RGB 34, 139, 34)
cor_fundo = (34, 139, 34)

# Defina as coordenadas da pista diagonal esquerda
# Por exemplo, um retângulo da parte inferior direita para a parte superior esquerda
pista_coords = [(largura, altura), (100, 100)]

while True:
    # Desenhe o fundo da tela como grama
    tela.fill(cor_fundo)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Desenhe a pista diagonal esquerda
    pygame.draw.polygon(tela, (0, 0, 0), pista_coords, 40)
    
    # Atualize e desenhe os obstáculos dentro do loop principal
    lista_de_obstaculos.update()
    lista_de_obstaculos.draw(tela)

    pygame.display.update()
