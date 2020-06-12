# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:55:12 2020

@author: Pedro Drumond
"""

#### POR ENQUANTO SEM FUNCIONALIDADE ####

import pygame
from ConfiguraçõesM import Config
from FunçõesM import TELA

CONFIGURACOES = Config()
TEXTOS = CONFIGURACOES.textos
CORES = CONFIGURACOES.cores



class Mapa(): # passar isso para dentro do Funções
    def __init__(self, tela, config): # não sei se precisa adicionar algo

        self.plano_de_fundo = pygame.image.load('mapa.png').convert_alpha() # carrega imagem do mapa
        self.plano_de_fundo = pygame.transform.scale(self.plano_de_fundo, (CONFIGURACOES.largura_tela_fundo, CONFIGURACOES.altura_tela_fundo))
        self.cell_largura = CONFIGURACOES.largura_tela_fundo//28
        self.cell_altura = CONFIGURACOES.altura_tela_fundo//30
        self.paredes = []  

    def tela_jogando(self, TELA): # imprime o mapa na tela
        TELA.blit(self.plano_de_fundo, (CONFIGURACOES.altura_topo_tela//2, CONFIGURACOES.altura_topo_tela//2))

        with open('Paredes.txt', 'r') as file:

        self.desenha_grid(TELA)
        pygame.display.update()
    
    def desenha_grid(self, TELA): # desenha os quadrados
        for x in range(CONFIGURACOES.largura_tela//self.cell_largura): # desenha linhas na vertical
            pygame.draw.line(self.plano_de_fundo, (255, 255, 255), (x*self.cell_largura, 0), (x*self.cell_largura, CONFIGURACOES.altura_tela))
        
        for x in range(CONFIGURACOES.altura_tela//self.cell_altura): # desenha linhas na horizontal
            pygame.draw.line(self.plano_de_fundo, (255, 255, 255), (0, x*self.cell_altura), (CONFIGURACOES.largura_tela, x*self.cell_altura))
