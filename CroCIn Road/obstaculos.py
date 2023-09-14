import pygame
import os

# Coordenadas dos obstáculos
coordenadas_obstaculos = [(100, 200), (400, 300), (700, 400)]

# Função para carregar e redimensionar uma imagem
def carregar_e_redimensionar_imagem(nome_arquivo, novo_tamanho):
    # Obtém o diretório atual do arquivo obstaculos.py
    current_dir = os.path.dirname(__file__)
    
    # Carrega a imagem
    imagem = pygame.image.load(os.path.join(current_dir, 'imagens', nome_arquivo))
    
    # Redimensiona a imagem para o tamanho desejado
    imagem = pygame.transform.scale(imagem, novo_tamanho)
    
    return imagem

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem):
        super().__init__()

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def cria_obstaculos():
    lista_de_obstaculos = pygame.sprite.Group()

    for x, y in coordenadas_obstaculos:
        # Carregar e redimensionar a imagem dentro do loop
        imagem = carregar_e_redimensionar_imagem('tree.jpg', (50, 50))  # Ajuste o tamanho conforme necessário
        obstaculo = Obstaculo(x, y, imagem)
        lista_de_obstaculos.add(obstaculo)

    return lista_de_obstaculos

# Crie a lista de obstáculos fora do loop principal
lista_de_obstaculos = cria_obstaculos()
