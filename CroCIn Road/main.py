import pygame
from pygame.locals import *
from sys import exit
from car import RightCar, LeftCar, spawn_carro_azul, spawn_carro_vermelho, remove_carros_fora_da_tela, atualizar_tempos_spawnagem
from personagem import Personagem
from cenario import Cenario
from settings import largura, altura, tempo_de_spawn_carro_azul, tempo_de_spawn_carro_vermelho, tamanho_personagem, cor_fundo, cor_texto, posicao_inicial_personagem
from coletaveis import Coletavel
from random import randint

pygame.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("CroCIn Road")

# Criando o personagem 
personagem = Personagem(
    posicao_inicial_personagem[0], posicao_inicial_personagem[1], tamanho_personagem, tela
)

coca_cafe = Coletavel(400, 400, 'coca_cafe.png', tela)
marmita = Coletavel(300, 300, 'marmita.png', tela)
coxinha = Coletavel(200, 200, 'coxinha.png', tela)

lista_coletaveis = (coca_cafe, marmita, coxinha)

carros_azuis = []
carros_vermelhos = []
posicoes_ocupadas_vermelhas = []

cenario = Cenario(largura, altura)

# Tempos da última spawnagem para carros azuis e vermelhos
ultima_spawnagem_azul = atualizar_tempos_spawnagem()
ultima_spawnagem_vermelho = atualizar_tempos_spawnagem()

while True:
    pygame.font.init()

    tela.fill(cor_fundo)
    
    # Desenho do cenário
    cenario.desenhar(tela)

    fonte_vidas = pygame.font.SysFont("bahnschrift", 25)
    fonte_coletaveis = pygame.font.SysFont("bahnschrift", 20)

    contador_vidas = fonte_vidas.render(f"Vidas: {personagem.vidas}", 1, cor_texto)
    tela.blit(contador_vidas, (500, 750))

    contador_cocas = fonte_coletaveis.render(f"Cocas: {personagem.cocas}", 1, cor_texto)
    tela.blit(contador_cocas, (25, 750))
    
    contador_marmitas = fonte_coletaveis.render(f"Marmitas: {personagem.marmitas}", 1, cor_texto)
    tela.blit(contador_marmitas, (125, 750))
    
    contador_coxinhas = fonte_coletaveis.render(f"Coxinhas: {personagem.coxinhas}", 1, cor_texto)
    tela.blit(contador_coxinhas, (250, 750))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Checa se é hora de fazer spawn de um novo carro azul
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - ultima_spawnagem_azul >= tempo_de_spawn_carro_azul:
        spawn_carro_azul(carros_azuis, largura)  # Use a função em car.py
        ultima_spawnagem_azul = atualizar_tempos_spawnagem()  # Atualize o tempo

    # Checa se é hora de fazer spawn de um novo carro vermelho
    if tempo_atual - ultima_spawnagem_vermelho >= tempo_de_spawn_carro_vermelho:
        spawn_carro_vermelho(carros_vermelhos, largura)  # Use a função em car.py
        ultima_spawnagem_vermelho = atualizar_tempos_spawnagem()  # Atualize o tempo
    
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

    remove_carros_fora_da_tela(carros_azuis, carros_vermelhos, posicoes_ocupadas_vermelhas)  # Use a função em car.py

    for coletavel in lista_coletaveis:
        colisao = coletavel.check_colisao(personagem.hitbox)
        if colisao:
            if lista_coletaveis.index(coletavel) == 0: #Coca-café
                personagem.cocas += 1
            elif lista_coletaveis.index(coletavel) == 1: #Marmita
                personagem.marmitas += 1
            elif lista_coletaveis.index(coletavel) == 2: #Coxinha
                personagem.coxinhas += 1
            coletavel.x = randint(100, 500)
            coletavel.y = randint(100, 700)
        
    # Chama a função de processar eventos do personagem
    personagem.processar_eventos()

    personagem.draw(tela)
    
    for coletavel in lista_coletaveis:
        coletavel.draw(tela)

    pygame.display.update()
