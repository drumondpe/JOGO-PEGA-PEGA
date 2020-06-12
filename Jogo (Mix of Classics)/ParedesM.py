# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:55:12 2020

@author: Pedro Drumond
"""

#### POR ENQUANTO SEM FUNCIONALIDADE ####

import pygame
import math
from ConfiguraçõesM import Config
from FunçõesM import TELA
vetor = pygame.math.Vector2

CONFIGURACOES = Config()
TEXTOS = CONFIGURACOES.textos
CORES = CONFIGURACOES.cores



class Mapa(): # passar isso para dentro do Funções
    def __init__(self, tela, config): #faz as variáveis dentro da classe Mapa

        self.plano_de_fundo = pygame.image.load('mapa.png').convert_alpha() # carrega imagem do mapa
        self.plano_de_fundo = pygame.transform.scale(self.plano_de_fundo, (CONFIGURACOES.largura_tela_fundo, CONFIGURACOES.altura_tela_fundo))
        self.cell_largura = CONFIGURACOES.largura_tela_fundo//28
        self.cell_altura = CONFIGURACOES.altura_tela_fundo//30
        self.paredes = []  

    def tela_jogando(self, TELA): # imprime o mapa na tela (com as paredes?)
        TELA.blit(self.plano_de_fundo, (CONFIGURACOES.altura_topo_tela//2, CONFIGURACOES.altura_topo_tela//2))

        with open('Paredes.txt', 'r') as file:     #abri o arquivo binário e cria uma lista para as paredes
            for y, linha in enumerate (file):
                for x, binario in enumerate(linha):
                    if binario == '1':
                        self.paredes.append(vetor(x, y))     #verificar vetor 

        self.desenha_grid(TELA)
        pygame.display.update()
    
    def desenha_grid(self, TELA): # desenha os quadrados
        for i in range(CONFIGURACOES.largura_tela//self.cell_largura): # desenha linhas na vertical
            pygame.draw.line(self.plano_de_fundo, (255, 255, 255), (i*self.cell_largura, 0), (i*self.cell_largura, CONFIGURACOES.altura_tela))
        
        for i in range(CONFIGURACOES.altura_tela//self.cell_altura): # desenha linhas na horizontal
            pygame.draw.line(self.plano_de_fundo, (255, 255, 255), (0, i*self.cell_altura), (CONFIGURACOES.largura_tela, i*self.cell_altura))

        for parede in self.paredes:
            pygame.draw.rect(self.plano_de_fundo, (CORES.aqua), (parede.x*self.cell_largura, parede.y*self.cell_altura, self.cell_largura, self.cell_altura))
        