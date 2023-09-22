import pygame
from pygame.locals import *
from sys import exit
from car import LeftCar, RightVan, RightCar
from personagem import Personagem
from cenario import Cenario

pygame.init()

# Defina o tempo de spawn para cada tipo de carro (em milissegundos)
tempo_de_spawn_carro_azul = 1000  # 3 segundos
tempo_de_spawn_carro_vermelho = 1500  # 2 segundos
tempo_de_spawn_van_direita = 8000

largura = 600
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("CroCIn Road")

tamanho = 40

# Defina a posição inicial do personagem
posicao_inicial_personagem = (largura / 2 - tamanho / 2, altura - 75)

# Posições fixas para o spawn do carro vermelho e da van
posicao_spawn_vermelho = (largura, 430)
posicao_spawn_van = (largura, 430)

# Variáveis para controlar o tempo desde o último spawn
ultima_spawnagem_azul = pygame.time.get_ticks()
ultima_spawnagem_vermelho = pygame.time.get_ticks()
ultima_spawnagem_van = pygame.time.get_ticks()

# Cor de fundo verde mais escuro (por exemplo, RGB 34, 139, 34)
cor_fundo = (34, 139, 34)

cenario = Cenario(largura, altura)

# Criando o personagem
personagem = Personagem(
    posicao_inicial_personagem[0], posicao_inicial_personagem[1], tamanho, tela
)

carros_azuis = []
carros_vermelhos = []
van = []

def spawn_carro_azul():
    carros_azuis.append(LeftCar(-70, 570, 5, largura))

def spawn_carro_vermelho():
    carros_vermelhos.append(RightCar(*posicao_spawn_vermelho, 2, largura))

def spawn_van_direita_van():
    van.append(RightVan(*posicao_spawn_van, 2, largura))

def remove_carros_fora_da_tela():
    for carro in carros_azuis[:]:
        if carro.x > 600:
            carros_azuis.remove(carro)
    for carro in carros_vermelhos[:]:
        if carro.x < -70:
            carros_vermelhos.remove(carro)
    
    for carro in van[:]:
        if carro.x < -70:
            van.remove(carro)

while True:
    # Desenho do cenário
    cenario.desenhar(tela)

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

    # Checa se é hora de fazer spawn de uma nova van
    if tempo_atual - ultima_spawnagem_van >= tempo_de_spawn_van_direita:
        spawn_van_direita_van()
        ultima_spawnagem_van = tempo_atual

    # Checando colisão dos carros azuis
    for carro in carros_azuis:
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

    # Checando colisão dos carros vermelhos
    for carro in carros_vermelhos:
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

    # Checando colisão das vans
    for carro in van:
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

    # Desenhar e mover os carros azuis
    for carro in carros_azuis:
        carro.draw(tela)
        carro.drive()

    # Desenhar e mover os carros vermelhos
    for carro in carros_vermelhos:
        carro.draw(tela)
        carro.drive()

    # Desenhar e mover as vans
    for carro in van:
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
