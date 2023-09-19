import pygame
import os

# Coordenadas e tamanhos dos obstáculos
obstaculos_info = [
    {"coordenadas": (200, 200), "tamanho": (100, 100), "imagem": "tree.png"},
    {"coordenadas": (300, 300), "tamanho": (150, 150), "imagem": "predio1.png"},
    {"coordenadas": (400, 400), "tamanho": (100, 100), "imagem": "tree.png"},
    {"coordenadas": (500, 500), "tamanho": (150, 150), "imagem": "predio1.png"},
    {"coordenadas": (600, 600), "tamanho": (150, 150), "imagem": "predio2.png"},
]


# Função para carregar e redimensionar uma imagem
def carregar_e_redimensionar_imagem(nome_arquivo, novo_tamanho):
    # Obtém o diretório atual do arquivo obstaculos.py
    current_dir = os.path.dirname(__file__)

    # Carrega a imagem
    imagem = pygame.image.load(os.path.join(current_dir, "imagens", nome_arquivo))

    # Redimensiona a imagem para o tamanho desejado
    imagem = pygame.transform.scale(imagem, novo_tamanho)

    return imagem


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y, tamanho, imagem):
        super().__init__()

        self.image = carregar_e_redimensionar_imagem(imagem, tamanho)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def cria_obstaculos():
    lista_de_obstaculos = pygame.sprite.Group()

    for obstaculo_info in obstaculos_info:
        x, y = obstaculo_info["coordenadas"]
        tamanho = obstaculo_info["tamanho"]
        imagem = obstaculo_info["imagem"]
        obstaculo = Obstaculo(x, y, tamanho, imagem)
        lista_de_obstaculos.add(obstaculo)

    return lista_de_obstaculos


# Lista de obstáculos exportada para ser usada em main.py
lista_de_obstaculos = cria_obstaculos()
