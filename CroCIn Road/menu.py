import pygame
from pygame.locals import *
import os

class Menu:
    def __init__(self):
        self.current_dir = os.path.dirname(__file__)
        
        self.background = pygame.image.load(os.path.join(self.current_dir, "imagens", "fundo_menu.jpg"))
        self.start_button = pygame.image.load(os.path.join(self.current_dir, "imagens", "botao_jogar.png"))
        self.exit_button = pygame.image.load(os.path.join(self.current_dir, "imagens", "botao_sair.png"))
    
    def desenhar(self, tela):
        tela.blit(self.background, (0, 0))
        tela.blit(self.start_button, (175, 320))
        tela.blit(self.exit_button, (175, 465))
    
    def verifica_clique(self, click_position):
        start = False
        sair = False
        
        # Verifica o botão de start
        if (
            click_position[0] <= 440 and click_position[0] >= 180
            and click_position[1] <= 408 and click_position[1] >= 326
        ):
            start = True
        # Verifica o botão de exit
        elif (
            click_position[0] <= 440 and click_position[0] >= 180
            and click_position[1] <= 560 and click_position[1] >= 470
        ):
            sair = True
        
        return start, sair

def executa_menu(menu, tela):
    
    start, sair = False, False
    
    # Loop de execução do menu
    while True:
        # Desenhando o menu na tela
        menu.desenhar(tela)
        
        for event in pygame.event.get():
            # Verifica o fim da execução do programa
            if event.type == QUIT:
                pygame.quit()
                exit()
            # Verifica se houve um clique no botão do mouse e se o botão foi o esquerdo
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # Verifica qual dos botões do menu foi selecionado
                start, sair = menu.verifica_clique(pygame.mouse.get_pos())
        
        if start:
            break
        elif sair:
            pygame.quit()
            exit()
        
        pygame.display.update()