import pygame
from pygame.locals import *
from sys import exit
from car import RightCar, LeftCar  
from personagem import Personagem
from cenario import Cenario
import time 

pygame.init()

largura = 600
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("CroCIn Road")

tamanho = 40

# Criando o personagem 
personagem = Personagem(
    largura / 2 - tamanho / 2, altura - 75, tamanho, tela
) 

# Criando os carros na direita, posição e velocidade
car1 = RightCar(700, 460, 2, largura)

# Criando os carros na esquerda, posição e velocidade
carro1_esquerda = LeftCar(-70, 570, 2)

# Cor de fundo verde mais escuro (por exemplo, RGB 34, 139, 34)
cor_fundo = (34, 139, 34)

cenario = Cenario(largura, altura)

while True:
    
    # Desenho do cenário
    cenario.desenhar(tela)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Checando colisão dos carros na direita
    colisao1 = car1.check_colisao(car1.x, car1.y, personagem.x, personagem.y)
    if colisao1:
        time.sleep(0.05)
        print('GAME OVER')
        break

    # Checando colisão dos carros na esquerda
    colisao2 = carro1_esquerda.check_colisao(carro1_esquerda.x, carro1_esquerda.y, personagem.x, personagem.y)
    if colisao2:
        time.sleep(0.05)
        print('GAME OVER')
        break
    
    # Desenhar os carros 
    car1.draw(tela)
    car1.drive()
    car1.check_boundary()
    
    carro1_esquerda.draw(tela)
    carro1_esquerda.drive()
    carro1_esquerda.check_boundary()

    # Chama a função de processar eventos do personagem
    personagem.processar_eventos()

    # Desenhar o personagem
    pygame.draw.rect(
        tela, personagem.cor, (personagem.x, personagem.y, personagem.tamanho, personagem.tamanho)
    )

    pygame.display.update()

    pygame.display.update()
