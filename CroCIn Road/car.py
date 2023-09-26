import pygame
import os

# Obtenha o caminho para a pasta "imagens" a partir do diretório atual
image_dir = os.path.join(os.path.dirname(__file__), 'imagens')

# Classe base para carros
class Car:
    def __init__(self, x, y, x_change, largura, image_filename):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.largura = largura
        original_image = pygame.image.load(os.path.join(image_dir, image_filename))
        self.image = pygame.transform.scale(original_image, (80, 50))  # Redimensionar a imagem
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.hitbox.topleft = (self.x, self.y)  # Atualizar a posição do hitbox

    def drive(self):
        pass  # A implementação específica será feita nas classes derivadas

    def check_boundary(self):
        pass  # A implementação específica será feita nas classes derivadas

    def check_colisao(self, player_hitbox):
        # Verifique a colisão usando o hitbox do jogador
        return self.hitbox.colliderect(player_hitbox)

# Classe derivada para o carro que se move para a direita
class RightCar(Car):
    def __init__(self, x, y, x_change, largura):
        super().__init__(x, y, x_change, largura, 'carredright.png')

    def drive(self):
        self.x -= self.x_change
        self.hitbox.topleft = (self.x, self.y)  # Atualizar a posição do hitbox

    def check_boundary(self):
        if self.x < -70:
            self.x = self.largura

# Classe derivada para o carro que se move para a esquerda
class LeftCar(Car):
    def __init__(self, x, y, x_change, largura):
        super().__init__(x, y, x_change, largura, 'carblue.png')

    def drive(self):
        self.x += self.x_change
        self.hitbox.topleft = (self.x, self.y)  # Atualizar a posição do hitbox

    def check_boundary(self):
        if self.x > 600:
            self.x = -70

def spawn_carro_azul(carros_azuis, largura):
    carros_azuis.append(LeftCar(-70, 570, 3, largura))

def spawn_carro_vermelho(carros_vermelhos, largura):
    carros_vermelhos.append(RightCar(700, 460, 4, largura))

def remove_carros_fora_da_tela(carros_azuis, carros_vermelhos, posicoes_ocupadas_vermelhas):
    for carro in carros_azuis[:]:
        if carro.x > 600:
            carros_azuis.remove(carro)
    for carro in carros_vermelhos[:]:
        if carro.x < -70:
            carros_vermelhos.remove(carro)
            if posicoes_ocupadas_vermelhas:
                posicoes_ocupadas_vermelhas.pop(0)

def atualizar_tempos_spawnagem():
    return pygame.time.get_ticks()

posicoes_ocupadas_vermelhas = []
