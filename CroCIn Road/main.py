import pygame
from pygame.locals import *
from sys import exit
from car import spawn_carro_azul, spawn_carro_vermelho, spawn_van, spawn_truck, remove_carros_fora_da_tela, atualizar_tempos_spawnagem
from personagem import Personagem
from cenario import Cenario
from menu import Menu
from settings import largura, altura, tempo_de_spawn_vans, tempo_de_spawn_trucks, tempo_de_spawn_carro_azul, tempo_de_spawn_carro_vermelho, tamanho_personagem, cor_texto, posicao_inicial_personagem
from coletaveis import Coletavel

# Inicializa a biblioteca PyGame
pygame.init()

# Inicializa o mixer da biblioteca PyGame
pygame.mixer.init()

# Criando o objeto 'tela' para o display de jogo e definindo o nome inserido na janela de execução
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("CroCIn Road")

menu = Menu()

def main(tela, menu):
    
    vitoria = False
    
    menu.executa_menu(tela)
    
    # Criando o personagem 
    personagem = Personagem(
        posicao_inicial_personagem[0], posicao_inicial_personagem[1], tamanho_personagem, tela
    )

    # Criando os coletáveis e listando-os
    coca_cafe = Coletavel(400, 400, 'coca_cafe.png', tela)
    marmita = Coletavel(300, 300, 'marmita.png', tela)
    coxinha = Coletavel(200, 200, 'coxinha.png', tela)

    lista_coletaveis = [coca_cafe, marmita, coxinha]

    carros_azuis = []
    carros_vermelhos = []
    vans = []
    trucks = []

    # Criando o objeto 'cenário', em que os elementos de ambiente são implementados
    cenario = Cenario(largura, altura)

    # Tempos da última spawnagem para carros azuis e vermelhos
    ultima_spawnagem_azul = atualizar_tempos_spawnagem()
    ultima_spawnagem_vermelho = atualizar_tempos_spawnagem()
    ultima_spawnagem_vans = atualizar_tempos_spawnagem()
    ultima_spawnagem_trucks = atualizar_tempos_spawnagem()

    while True:
        # Inicializa o módulo de fontes do PyGame
        pygame.font.init()
        
        # Desenho do cenário
        cenario.desenhar(tela)
        
        # Desenho dos coletáveis na tela
        for coletavel in lista_coletaveis:
            coletavel.draw(tela)
        
        # Desenho do personagem na tela
        personagem.draw(tela)

        # Cria as fontes associadas às caixas de texto usadas na contagem de vidas e de coletáveis
        fonte_vidas = pygame.font.SysFont("bahnschrift", 25)
        fonte_coletaveis = pygame.font.SysFont("bahnschrift", 20)

        # Instancia e coloca na tela cada um dos contadores usados
        contador_vidas = fonte_vidas.render(f"Vidas: {personagem.vidas}", 1, cor_texto)
        tela.blit(contador_vidas, (500, 750))

        contador_cocas = fonte_coletaveis.render(f"Cocas: {personagem.cocas}", 1, cor_texto)
        tela.blit(contador_cocas, (25, 750))
        
        contador_marmitas = fonte_coletaveis.render(f"Marmitas: {personagem.marmitas}", 1, cor_texto)
        tela.blit(contador_marmitas, (125, 750))
        
        contador_coxinhas = fonte_coletaveis.render(f"Coxinhas: {personagem.coxinhas}", 1, cor_texto)
        tela.blit(contador_coxinhas, (250, 750))

        # Verifica o fim da execução do programa
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
        
        # Checa se é hora de fazer spawn de uma nova van
        if tempo_atual - ultima_spawnagem_vans >= tempo_de_spawn_vans:
            spawn_van(vans, largura)  # Use a função em car.py
            ultima_spawnagem_vans = atualizar_tempos_spawnagem()  # Atualize o tempo
        
        # Checa se é hora de fazer spawn de um novo truck
        if tempo_atual - ultima_spawnagem_trucks >= tempo_de_spawn_trucks:
            spawn_truck(trucks, largura)  # Use a função em car.py
            ultima_spawnagem_trucks = atualizar_tempos_spawnagem()  # Atualize o tempo
        
        # Instancia cada tipo de veículo em uma tupla
        tipos_carro = (carros_vermelhos, carros_azuis, vans, trucks)

        # Checando colisão com os carros
        for tipo_carro in tipos_carro:
            for carro in tipo_carro:
                colisao = carro.check_colisao(personagem.hitbox)
                if colisao:
                    pygame.mixer.music.load("sons\car_hit.wav")
                    pygame.mixer.music.play()
                    
                    personagem.vidas -= 1  # Decrementa a vida do personagem
                    print(f'Vidas restantes: {personagem.vidas}') # Imprime o número de vidas restantes no terminal
                    
                    # Verifica se o jogador perdeu todas as vidas restantes
                    if personagem.vidas <= 0:
                        pygame.mixer.music.load("sons\game_over.wav")
                        pygame.mixer.music.play()
                        
                        while pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(10)
                        
                        print('GAME OVER')
                        
                        # Removendo carros desenhados anteriormente
                        remove_carros_fora_da_tela(carros_azuis, carros_vermelhos, vans, trucks)
                        for tipo_carro in tipos_carro:
                            for carro in tipo_carro:
                                tipo_carro.remove(carro)
                        
                        pygame.display.update()
                        
                        main(tela, menu)
                    else:
                        # Reseta a posição do personagem para a inicial
                        personagem.x, personagem.y = posicao_inicial_personagem
        
        # Desenhar e mover os carros na tela
        for tipo_carro in tipos_carro:
            for carro in tipo_carro:
                carro.draw(tela)
                carro.drive()

        remove_carros_fora_da_tela(carros_azuis, carros_vermelhos, vans, trucks)  

        # Checando colisão com os coletáveis e incrementando sua quantidade nos atributos do personagem
        for coletavel in lista_coletaveis:
            colisao = coletavel.check_colisao(personagem.hitbox)
            if colisao:
                pygame.mixer.music.load("sons\get_coletavel.wav")
                pygame.mixer.music.play()
                
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
            and personagem.y <= 30 # Linha de chegada
        ):
            if not vitoria:
                pygame.mixer.music.load("sons\win.wav")
                pygame.mixer.music.play()
            
            vitoria = True
            
            fonte_vitoria = pygame.font.SysFont("bahnschrift", 45)
            texto_vitoria = fonte_vitoria.render("You Won!", 1, cor_texto)

            fonte_vitoria = pygame.font.SysFont(
                "bahnschrift", 20
            )
            texto_continua = fonte_vitoria.render(
                "(Press 'S' to go to menu or 'N' to exit)", 1, cor_texto
            )

            tela.blit(texto_vitoria, (215, 350))
            tela.blit(texto_continua, (145, 395))


            response = pygame.key.get_pressed()

            # Verifica se o jogo continuará ou não, de acordo com a última tecla pressionada
            if response[pygame.K_s]:
                main(tela, menu)
            elif response[pygame.K_n]:
                pygame.quit()
                exit()
        
        # Chama a função de processar eventos do personagem
        personagem.processar_eventos()

        # Atualiza o display com os últimos eventos processados
        pygame.display.update()

if __name__ == '__main__':
    main(tela, menu)
