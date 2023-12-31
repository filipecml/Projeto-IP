import pygame
import os

image_dir = os.path.join(os.path.dirname(__file__), "imagens")


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
        self.vidas = 3
        self.marmitas = 0
        self.cocas = 0
        self.coxinhas = 0
        self.sprite_variation = 0

        self.original_images = {
            "left": [pygame.image.load(
                os.path.join(image_dir, "personagem_andando_esquerda1.png")),
                    pygame.image.load(
                os.path.join(image_dir, "personagem_andando_esquerda2.png"))],
            "right": [pygame.image.load(
                os.path.join(image_dir, "personagem_andando_direita1.png")),
                    pygame.image.load(
                os.path.join(image_dir, "personagem_andando_direita2.png"))],
            "up": [pygame.image.load(
                os.path.join(image_dir, "personagem_andando_costas1.png")),
                    pygame.image.load(
                os.path.join(image_dir, "personagem_andando_costas2.png"))],
            "down": [pygame.image.load(
                os.path.join(image_dir, "personagem_andando_frente1.png")),
                    pygame.image.load(
                os.path.join(image_dir, "personagem_andando_frente2.png"))],
            "still": pygame.image.load(
                os.path.join(image_dir, "personagem_parado_costas.png")),
        }

        self.image = pygame.transform.scale(
            self.original_images["still"], (self.tamanho, self.tamanho)
        )  # Redimensionar a imagem

        self.is_moving = False
        self.movement_step = self.tamanho
        self.hitbox = pygame.Rect(self.x, self.y, tamanho, tamanho)

    def movimento(self, dx, dy):
        # Atualize a posição do personagem
        self.x += dx
        self.y += dy

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.hitbox.topleft = (self.x, self.y)  # Atualizar a posição do hitbox

    def reset_status(self):
        self.vidas = 3
        self.cocas = 0
        self.marmitas = 0
        self.coxinhas = 0

    def check_sprite_variation(self):
        if self.sprite_variation == 0:
            self.sprite_variation = 1
        else:
            self.sprite_variation = 0

    def processar_eventos(self):
        keys = pygame.key.get_pressed()

        self.hitbox.x = self.x
        self.hitbox.y = self.y

        # Se o personagem não estiver em movimento e uma tecla for pressionada
        if not self.is_moving:
            
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.movimento(-self.movement_step, 0)
                self.image = pygame.transform.scale(
                    self.original_images["left"][self.sprite_variation], (self.tamanho, self.tamanho)
                )
                self.is_moving = True
                self.check_sprite_variation()
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.movimento(self.movement_step, 0)
                self.image = pygame.transform.scale(
                    self.original_images["right"][self.sprite_variation], (self.tamanho, self.tamanho)
                )
                self.is_moving = True
                self.check_sprite_variation()
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                self.movimento(0, -self.movement_step)
                self.image = pygame.transform.scale(
                    self.original_images["up"][self.sprite_variation], (self.tamanho, self.tamanho)
                )
                self.is_moving = True
                self.check_sprite_variation()
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.movimento(0, self.movement_step)
                self.image = pygame.transform.scale(
                    self.original_images["down"][self.sprite_variation], (self.tamanho, self.tamanho)
                )
                self.is_moving = True
                self.check_sprite_variation()

        # Se uma tecla diferente for pressionada, pare o movimento
        elif not (
            keys[pygame.K_LEFT]
            or keys[pygame.K_a]
            or keys[pygame.K_RIGHT]
            or keys[pygame.K_d]
            or keys[pygame.K_UP]
            or keys[pygame.K_w]
            or keys[pygame.K_DOWN]
            or keys[pygame.K_s]
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
