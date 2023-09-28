import pygame
import os

# Configurações da tela
largura = 600
altura = 800

# Configurações dos carros
tempo_de_spawn_carro_azul = 1750
tempo_de_spawn_carro_vermelho = 2000
tempo_de_spawn_vans = 2500
tempo_de_spawn_trucks = 3000

# Tamanho do personagem
tamanho_personagem = 40

# Cores
cor_fundo = (34, 139, 34)
cor_texto = (0, 0, 0)

# Posição inicial do personagem
posicao_inicial_personagem = (largura / 2 - tamanho_personagem / 2, altura - 125)


image_dir = os.path.join(os.path.dirname(__file__), 'imagens')

