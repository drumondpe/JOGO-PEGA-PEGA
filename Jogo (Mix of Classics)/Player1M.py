# -*- coding: utf-8 -*-
"""
Classe dos Players

Authors: Keiya Nishio and Pedro Drumond
"""

import pygame
from ConfiguraçõesM import Config
from Player2M import Player2
CONFIGURACOES = Config()

class Player1(pygame.sprite.Sprite):
    #Classe que define o sprite do jogador

    def __init__(self, tela, config, mapa):
        #cria uma nova instância da classe Player1

        self.tela = tela
        self.config = config
        self.mapa = mapa
        self.image = pygame.image.load('pacman.png') 
        self.image = pygame.transform.scale(self.image, (23, 23))
        self.image.set_colorkey((0,0,0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.screen_rect = tela.get_rect()
        self.rect.centerx = self.screen_rect.centerx - 250
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom -605

        # propriedades customizadas de movimento
        self.velocidade1 = CONFIGURACOES.velocidade_player1 
        self.centro1 = [self.rect.centerx, self.rect.centery]

        #booleanos de movimento
        self.indo_para_cima1 = False
        self.indo_para_baixo1 = False
        self.indo_para_direita1 = False
        self.indo_para_esquerda1 = False


    def update(self):
        #atualiza posição do player conforme a velocidade

        x_antigo = self.centro1[0]
        y_antigo = self.centro1[1]
        if self.indo_para_cima1:
            self.centro1[1] -= self.velocidade1

        if self.indo_para_baixo1:
            self.centro1[1] += self.velocidade1

        if self.indo_para_direita1:
            self.centro1[0] += self.velocidade1

        if self.indo_para_esquerda1:
            self.centro1[0] -= self.velocidade1

        self.rect.centerx = self.centro1[0]
        self.rect.centery = self.centro1[1]

        colidiu = pygame.sprite.collide_mask(self, self.mapa) #colisão com a parede
        if colidiu:
            self.centro1[0] = x_antigo
            self.centro1[1] = y_antigo
            self.rect.centerx = self.centro1[0]
            self.rect.centery = self.centro1[1]

