import pygame
from pygame.locals import *
import os

class Menu:
    def __init__(self):
        self.current_dir = os.path.dirname(__file__)
        self.instrucoes = False
        
        self.background = pygame.image.load(os.path.join(self.current_dir, "imagens", "fundo_menu.jpg"))
        self.start_button = pygame.transform.scale(pygame.image.load(os.path.join(self.current_dir, "imagens", "botao_jogar.png")), (199, 72))
        self.exit_button = pygame.transform.scale(pygame.image.load(os.path.join(self.current_dir, "imagens", "botao_sair.png")), (199, 72))
        self.instructions_button = pygame.transform.scale(pygame.image.load(os.path.join(self.current_dir, "imagens", "botao_instrucoes.png")), (199, 72))
        self.instructions_text = pygame.image.load(os.path.join(self.current_dir, "imagens", "Instruções_com_fundo.jpg"))

        self.menu_music = os.path.join(self.current_dir, "sons", "menu_music.mp3")
        self.click_sound = os.path.join(self.current_dir, "sons", "click_on_menu.wav")

    def play_menu_music(self):
        pygame.mixer.music.load(self.menu_music)
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1)

    def desenhar(self, tela):
        tela.blit(self.background, (0, 0))
        tela.blit(self.start_button, (205, 300))
        tela.blit(self.exit_button, (205, 400))
        tela.blit(self.instructions_button, (205, 500))

    def verifica_clique(self, click_position):
        start, sair, instrucoes = False, False, False

        if (
            click_position[0] <= 405 and click_position[0] >= 205
            and click_position[1] <= 365 and click_position[1] >= 300
        ):
            start = True
        elif (
            click_position[0] <= 405 and click_position[0] >= 205
            and click_position[1] <= 465 and click_position[1] >= 405
        ):
            sair = True
        elif (
            click_position[0] <= 405 and click_position[0] >= 205
            and click_position[1] <= 565 and click_position[1] >= 505
        ):
            instrucoes = True

        return start, sair, instrucoes

    def mostra_instrucoes(self, tela):
        tela.blit(self.instructions_text, (0, 0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        response = pygame.key.get_pressed()
        if response[pygame.K_ESCAPE]:
            self.instrucoes = False  # Voltando para o menu
            self.play_menu_music()

    def executa_menu(self, tela):
        os.chdir(self.current_dir)

        self.play_menu_music()
        while True:
            self.desenhar(tela)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    start, sair, instrucoes = self.verifica_clique(pygame.mouse.get_pos())

                    if start:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(self.click_sound)
                        pygame.mixer.music.play()
                        return
                    elif instrucoes:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(self.click_sound)
                        pygame.mixer.music.play()
                        self.instrucoes = True
                    elif sair:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(self.click_sound)
                        pygame.mixer.music.play()
                        
                        while pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(5)
                            
                        pygame.quit()
                        exit()

            if self.instrucoes:
                self.mostra_instrucoes(tela)
            
            pygame.display.update()
