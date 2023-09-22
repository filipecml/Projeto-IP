import pygame
from pygame.locals import *
from sys import exit
from car import RightCar, LeftCar
from personagem import Personagem
from cenario import Cenario
import random

pygame.init()

# Defina o tempo de spawn para cada tipo de carro (em milissegundos)
tempo_de_spawn_carro_azul = 1000 
tempo_de_spawn_carro_vermelho = 1500

largura = 600
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("CroCIn Road")

tamanho = 40

# Defina a posição inicial do personagem
posicao_inicial_personagem = (largura / 2 - tamanho / 2, altura - 75)
posicoes_ocupadas_vermelhas = []

# Criando o personagem 
personagem = Personagem(
    posicao_inicial_personagem[0], posicao_inicial_personagem[1], tamanho, tela
) 

carros_azuis = []
carros_vermelhos = []

def spawn_carro_azul():
    carros_azuis.append(LeftCar(-70, 570, 5, largura))

def spawn_carro_vermelho():
    carros_vermelhos.append(RightCar(700, 460, 2, largura))

def remove_carros_fora_da_tela():
    for carro in carros_azuis[:]:
        if carro.x > 600:
            carros_azuis.remove(carro)
    for carro in carros_vermelhos[:]:
        if carro.x < -70:
            carros_vermelhos.remove(carro)
            # Remova a posição ocupada apenas se houver alguma na lista
            if posicoes_ocupadas_vermelhas:
                posicoes_ocupadas_vermelhas.pop(0)  # Remova a primeira posição

# Cor de fundo verde mais escuro (por exemplo, RGB 34, 139, 34)
cor_fundo = (34, 139, 34)

cenario = Cenario(largura, altura)

# Tempos da última spawnagem para carros azuis e vermelhos
ultima_spawnagem_azul = pygame.time.get_ticks()
ultima_spawnagem_vermelho = pygame.time.get_ticks()

while True:
    pygame.font.init()

    tela.fill(cor_fundo)
    
    # Desenho do cenário
    cenario.desenhar(tela)

    fonte = pygame.font.SysFont("bahnschrift", 25)

    contador_vidas = fonte.render(f"Vidas: {personagem.vidas}", 1, (0, 0, 0))
    tela.blit(contador_vidas, (450, 750))

    contador_coletaveis = fonte.render(f"Coletáveis: {personagem.coletaveis}", 1, (0, 0, 0))
    tela.blit(contador_coletaveis, (50, 750))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Checa se é hora de fazer spawn de um novo carro azul
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - ultima_spawnagem_azul >= tempo_de_spawn_carro_azul:
        spawn_carro_azul()
        ultima_spawnagem_azul = tempo_atual

    # Checa se é hora de fazer spawn de um novo carro vermelho
    if tempo_atual - ultima_spawnagem_vermelho >= tempo_de_spawn_carro_vermelho:
        spawn_carro_vermelho()
        ultima_spawnagem_vermelho = tempo_atual
    
    tipos_carro = (carros_vermelhos, carros_azuis)

    # Checando colisão com os carros
    for tipo_carro in tipos_carro:
        for carro in tipo_carro:
            colisao = carro.check_colisao(personagem.hitbox)
            if colisao:
                personagem.vidas -= 1  # Decrementa a vida do personagem
                print(f'Vidas restantes: {personagem.vidas}')
                if personagem.vidas <= 0:
                    print('GAME OVER')
                    pygame.quit()
                    exit()
                else:
                    # Redefina a posição do personagem para a posição inicial
                    personagem.x, personagem.y = posicao_inicial_personagem
    
    # Desenhar e mover os carros na tela
    for tipo_carro in tipos_carro:
        for carro in tipo_carro:
            carro.draw(tela)
            carro.drive()

    remove_carros_fora_da_tela()

    # Chama a função de processar eventos do personagem
    personagem.processar_eventos()

    # Desenhar o personagem
    pygame.draw.rect(
        tela, personagem.cor, (personagem.x, personagem.y, personagem.tamanho, personagem.tamanho)
    )

    pygame.display.update()
