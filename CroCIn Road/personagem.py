import pygame

class Personagem:
    def __init__(self, x, y, tamanho, tela):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.cor = (255, 255, 255)
        self.tela = tela
        self.velocidade = 1

    def criar_personagem(self):
        pygame.draw.rect(
            self.tela, self.cor, (self.x, self.y, self.tamanho, self.tamanho)
        )

    def movimento(self, dx, dy):
        # Atualize a posição do personagem
        self.x += dx
        self.y += dy

        # Verifique os limites da tela
        if self.x < 0:
            self.x = 0
        elif self.x + self.tamanho > self.tela.get_width():
            self.x = self.tela.get_width() - self.tamanho

        if self.y < 0:
            self.y = 0
        elif self.y + self.tamanho > self.tela.get_height():
            self.y = self.tela.get_height() - self.tamanho

    def processar_eventos(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.movimento(-self.velocidade, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.movimento(self.velocidade, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.movimento(0, -self.velocidade)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.movimento(0, self.velocidade)

        #COLOCAR EVENTO DE COLISÃO
        
