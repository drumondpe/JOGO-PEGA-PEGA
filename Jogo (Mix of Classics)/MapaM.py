# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:55:12 2020

@author: Pedro Drumond
"""

#### POR ENQUANTO SEM FUNCIONALIDADE ####

import pygame
import math
vetor = pygame.math.Vector2
from ConfiguraçõesM import Config
from FunçõesM import TELA

CONFIGURACOES = Config()
TEXTOS = CONFIGURACOES.textos
CORES = CONFIGURACOES.cores



class Mapa(pygame.sprite.Sprite):
    # Classe que define o sprite do mapa
    def __init__(self, tela, config):
        pygame.sprite.Sprite.__init__(self) 
        self.mask = pygame.image.load('mapa - mascara.png')
        self.mask = pygame.transform.scale(self.mask, (CONFIGURACOES.largura_tela_fundo, CONFIGURACOES.altura_tela_fundo))
        self.mask.set_colorkey((0, 0, 0))
        self.image = self.mask
        self.rect = self.image.get_rect()
        self.rect.x = CONFIGURACOES.altura_topo_tela//2
        self.rect.y = CONFIGURACOES.altura_topo_tela//2
        self.mask = pygame.mask.from_surface(self.mask)

    def tela_jogando(self, TELA): # imprime o mapa na tela
        TELA.blit(self.image, self.rect)
        
        pygame.display.update()
    
