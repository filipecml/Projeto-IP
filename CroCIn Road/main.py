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

#Criando o personagem 
personagem = Personagem(
    largura / 2 - tamanho / 2, altura - 75, tamanho, tela
) 

#Criando os carros, posição e velocidade
car1 = RightCar(300, 500, 1, largura)

# Cor de fundo verde mais escuro (por exemplo, RGB 34, 139, 34)
cor_fundo = (34, 139, 34)

cenario = Cenario(largura, altura)

while True:
    
    # Desenho do cenario
    cenario.desenhar(tela)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #Checando colisão dos carros
    colisao1 = car1.check_colisao(car1.x, car1.y, personagem.x, personagem.y)
    if colisao1:
        time.sleep(0.05)
        print('GAME OVER')
        break
    
    # Desenhar os carros 
    car1.draw(tela)
    car1.drive()
    car1.check_boundary()

    # Chama a função de processar eventos do personagem
    personagem.processar_eventos()

    # Desenhe o personagem
    personagem.criar_personagem()

    pygame.display.update()