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
        self.plano_de_fundo = pygame.transform.scale(self.plano_de_fundo, (CONFIGURACOES.largura_tela, CONFIGURACOES.altura_tela))

    def tela_jogando(self, TELA): # imprime o mapa na tela
        TELA.blit(self.plano_de_fundo, (0, 0))
        self.desenha_grid(TELA)
        pygame.display.update()
    
    def desenha_grid(self, TELA): # desenha os quadrados
        for i in range(CONFIGURACOES.largura_tela//self.cell_largura): # desenha linhas na vertical
            pygame.draw.line(self.tela, (255, 255, 255), (x*self.cell_largura, 0), (x*self.cell_altura, CONFIGURACOES.altura_tela))
        
        for i in range(CONFIGURACOES.altura_tela//self.cell_altura): # desenha linhas na horizontal
            pygame.draw.line(self.tela, (255, 255, 255), (0, x*self.cell_altura), (CONFIGURACOES.largura_tela, x*self.cell_altura))

