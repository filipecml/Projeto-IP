import pygame
from pygame.locals import *
from sys import exit
from car import spawn_carro_azul, spawn_carro_vermelho, spawn_van, spawn_truck, remove_carros_fora_da_tela, atualizar_tempos_spawnagem
from personagem import Personagem
from cenario import Cenario
from settings import largura, altura, tempo_de_spawn_vans, tempo_de_spawn_trucks, tempo_de_spawn_carro_azul, tempo_de_spawn_carro_vermelho, tamanho_personagem, cor_texto, posicao_inicial_personagem
from coletaveis import Coletavel

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

lista_coletaveis = [coca_cafe, marmita, coxinha]

carros_azuis = []
carros_vermelhos = []
vans = []
trucks = []

cenario = Cenario(largura, altura)

# Tempos da última spawnagem para carros azuis e vermelhos
ultima_spawnagem_azul = atualizar_tempos_spawnagem()
ultima_spawnagem_vermelho = atualizar_tempos_spawnagem()
ultima_spawnagem_vans = atualizar_tempos_spawnagem()
ultima_spawnagem_trucks = atualizar_tempos_spawnagem()

coletaveis_coletados = {
    "cocas": 0,
    "marmitas": 0,
    "coxinhas": 0
}

while True:
    vitoria = False
    
    pygame.font.init()
    
    # Desenho do cenário
    cenario.desenhar(tela)
    
    for coletavel in lista_coletaveis:
        coletavel.draw(tela)
    
    personagem.draw(tela)

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
    
    if tempo_atual - ultima_spawnagem_vans >= tempo_de_spawn_vans:
        spawn_van(vans, largura)  # Use a função em car.py
        ultima_spawnagem_vans = atualizar_tempos_spawnagem()  # Atualize o tempo
    
    if tempo_atual - ultima_spawnagem_trucks >= tempo_de_spawn_trucks:
        spawn_truck(trucks, largura)  # Use a função em car.py
        ultima_spawnagem_trucks = atualizar_tempos_spawnagem()  # Atualize o tempo
    
    tipos_carro = (carros_vermelhos, carros_azuis, vans, trucks)

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
                    personagem.x, personagem.y = posicao_inicial_personagem
    
    # Desenhar e mover os carros na tela
    for tipo_carro in tipos_carro:
        for carro in tipo_carro:
            carro.draw(tela)
            carro.drive()

    remove_carros_fora_da_tela(carros_azuis, carros_vermelhos, vans, trucks)  

    for coletavel in lista_coletaveis:
        colisao = coletavel.check_colisao(personagem.hitbox)
        if colisao:
            if lista_coletaveis.index(coletavel) == 0:  # Coca-café
                personagem.cocas += 1
            elif lista_coletaveis.index(coletavel) == 1:  # Marmita
                personagem.marmitas += 1
            elif lista_coletaveis.index(coletavel) == 2:  # Coxinha
                personagem.coxinhas += 1
            coletavel.cria_coletavel()

    #Verifica a vitoria 
    if (
        personagem.cocas >= 5
        and personagem.marmitas >= 5
        and personagem.coxinhas >= 5
        and personagem.y <= 30
    ):
        fonte_vitoria = pygame.font.SysFont("bahnschrift", 45)
        texto_vitoria = fonte_vitoria.render("You Won!", 1, cor_texto)

        fonte_vitoria = pygame.font.SysFont(
            "bahnschrift", 20
        )
        texto_continua = fonte_vitoria.render(
            "(Press 'S' to continue or 'N' to exit)", 1, cor_texto
        )

        tela.blit(texto_vitoria, (215, 350))
        tela.blit(texto_continua, (145, 395))

        continua = False

        response = pygame.key.get_pressed()

        if response[pygame.K_s]:
            continua = True

            for coletavel in lista_coletaveis:
                lista_coletaveis.remove(coletavel)

            lista_coletaveis = [coca_cafe, marmita, coxinha]
            for coletavel in lista_coletaveis:
                coletavel.cria_coletavel()

            personagem.reset_status()
            personagem.x = posicao_inicial_personagem[0]
            personagem.y = posicao_inicial_personagem[1]
        elif response[pygame.K_n]:
            pygame.quit()
            exit()
        vitoria = True
    
    # Chama a função de processar eventos do personagem
    if not vitoria or continua:
        personagem.processar_eventos()

    pygame.display.update()
