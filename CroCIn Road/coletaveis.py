import pygame
import os

# Coordenadas e tamanhos dos coletáveis
coletaveis_info = [
    {"coordenadas": (500, 500), "tamanho": (50, 50), "imagem": "coxinha.png"},
    {"coordenadas": (600, 300), "tamanho": (50, 50), "imagem": "marmita.png"},
    {"coordenadas": (1000, 500), "tamanho": (50, 50), "imagem": "coca_cafe.png"},
]


def carregar_e_redimensionar_imagem(nome_arquivo, novo_tamanho):
    # Obtém o diretório atual do arquivo coletaveis.py
    current_dir = os.path.dirname(__file__)

    # Carrega a imagem
    imagem = pygame.image.load(os.path.join(current_dir, "imagens", nome_arquivo))

    # Redimensiona a imagem para o tamanho desejado
    imagem = pygame.transform.scale(imagem, novo_tamanho)

    return imagem


class Coletavel(pygame.sprite.Sprite):
    def __init__(self, x, y, tamanho, imagem):
        super().__init__()

        self.image = carregar_e_redimensionar_imagem(imagem, tamanho)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def cria_coletaveis():
    lista_de_coletaveis = pygame.sprite.Group()

    for coletavel_info in coletaveis_info:
        x, y = coletavel_info["coordenadas"]
        tamanho = coletavel_info["tamanho"]
        imagem = coletavel_info["imagem"]
        coletavel = Coletavel(x, y, tamanho, imagem)
        lista_de_coletaveis.add(coletavel)

    return lista_de_coletaveis


# Lista de obstáculos exportada para ser usada em main.py
lista_de_coletaveis = cria_coletaveis()
