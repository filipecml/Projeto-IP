import pygame

class Personagem:
    
    def __init__(self, x, y, tamanho, tela):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.cor = (255, 255, 255)
        self.tela = tela
        self.velocidade_maxima = 2.0
        self.aceleracao = 0.1
        self.velocidade_atual = 0.0

        self.is_moving = False
        self.movement_step = self.tamanho

    def movimento(self, dx, dy):
        # Atualize a posição do personagem
        self.x += dx
        self.y += dy


    def processar_eventos(self):
        keys = pygame.key.get_pressed()
        
        # Se o personagem não estiver em movimento e uma tecla for pressionada
        if not self.is_moving:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.movimento(-self.movement_step, 0)
                self.is_moving = True
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.movimento(self.movement_step, 0)
                self.is_moving = True
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                self.movimento(0, -self.movement_step)
                self.is_moving = True
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.movimento(0, self.movement_step)
                self.is_moving = True

        # Se uma tecla diferente for pressionada, pare o movimento
        elif (
            not (keys[pygame.K_LEFT] or keys[pygame.K_a] or
                 keys[pygame.K_RIGHT] or keys[pygame.K_d] or
                 keys[pygame.K_UP] or keys[pygame.K_w] or
                 keys[pygame.K_DOWN] or keys[pygame.K_s])
        ):
            self.is_moving = False

        # Verifique os limites da tela
        if self.x < 0:
            self.x = 0
        elif self.x + self.tamanho > self.tela.get_width():
            self.x = self.tela.get_width() - self.tamanho

        if self.y < 0:
            self.y = 0
        elif self.y + self.tamanho > self.tela.get_height():
            self.y = self.tela.get_height() - self.tamanho
