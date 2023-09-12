import pygame as pg
import sys
import random

import Logica
import Classes

#Inicializa o funcionamento do PyGame
pg.init()

#Inicializa o looping de execução e sua variável de controle
running = True
while(running):
    for event in pygame.event.get():
        #Verifica se houve a solicitação de fim da execução do programa
        if event.type == pygame.QUIT:
            running = False
    
