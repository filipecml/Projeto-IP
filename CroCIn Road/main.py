import pygame
from pygame.locals import *
from sys import exit
from car import RightCar, LeftCar
from personagem import Personagem
from cenario import Cenario
import time

pygame.init()

# Defina o tempo de spawn para cada tipo de carro (em milissegundos)
tempo_de_spawn_carro_azul = 1000  # 3 segundos
tempo_de_spawn_carro_vermelho = 1000  # 2 segundos

largura = 600
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("CroCIn Road")

tamanho = 40

# Criando o personagem
personagem = Personagem(
    largura / 2 - tamanho / 2, altura - 75, tamanho, tela
)

# Criando os carros, posição e velocidade
car1 = RightCar(300, 500, 1, largura)

# Cor de fundo verde mais escuro (por exemplo, RGB 34, 139, 34)
cor_fundo = (34, 139, 34)

cenario = Cenario(largura, altura)

# Tempos da última spawnagem para carros azuis e vermelhos
ultima_spawnagem_azul = pygame.time.get_ticks()
ultima_spawnagem_vermelho = pygame.time.get_ticks()

while True:
    # Preencher a tela com a cor de fundo para limpar o quadro anterior
    tela.fill(cor_fundo)

    # Desenho do cenario
    cenario.desenhar(tela)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Checando colisão dos carros
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

    # Desenhar o personagem
    pygame.draw.rect(
        tela, personagem.cor, (personagem.x, personagem.y, personagem.tamanho, personagem.tamanho)
    )

    pygame.display.update()
