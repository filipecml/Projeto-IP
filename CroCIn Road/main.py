<<<<<<< Updated upstream
import pygame as pg
import sys
import random
=======
import pygame
from pygame.locals import *
from sys import exit
from obstaculos import lista_de_obstaculos
from personagem import Personagem
>>>>>>> Stashed changes

#Inicializa o funcionamento do PyGame
pg.init()

<<<<<<< Updated upstream
=======
largura = 1280
altura = 720

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("CroCIn Road")

personagem = Personagem(15, altura / 2, 50, tela)


def movimentacao(personagem):
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] or keys[K_a]:
        personagem.movimento(-personagem.velocidade, 0)
    if keys[K_RIGHT] or keys[K_d]:
        personagem.movimento(personagem.velocidade, 0)
    if keys[K_UP] or keys[K_w]:
        personagem.movimento(0, -personagem.velocidade)
    if keys[K_DOWN] or keys[K_s]:
        personagem.movimento(0, personagem.velocidade)


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

    # Chame a função de movimentação do personagem
    movimentacao(personagem)

    # Desenhe o personagem
    personagem.criar_personagem()

    pygame.display.update()
>>>>>>> Stashed changes
