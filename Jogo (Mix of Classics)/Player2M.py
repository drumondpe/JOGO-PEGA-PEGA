# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:55:12 2020

@author: Pedro Drumond
"""
import pygame
from ConfiguraçõesM import Config
CONFIGURACOES = Config()

class Player2(pygame.sprite.Sprite):
    #Classe que define o sprite do jogador

    def __init__(self, tela, config, mapa):
    #cria uma nova instância da classe Player2

        self.tela = tela
        self.config = config
        self.mapa = mapa
        self.image = pygame.image.load('pacman-azul.png') #mudar foto do player ou fotos
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.screen_rect = tela.get_rect()
        self.rect.centerx = self.screen_rect.centerx + 250
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom - 45

        # propriedades customizadas de movimento
        self.velocidade2 = CONFIGURACOES.velocidade #VERIFICAR
        self.centro2 = [self.rect.centerx, self.rect.centery]

        #booleanos de movimento
        self.indo_para_cima2 = False
        self.indo_para_baixo2 = False
        self.indo_para_direita2 = False
        self.indo_para_esquerda2 = False

    def update(self):
        #atualiza posição do player conforme a velocidade

        x_antigo = self.centro2[0]
        y_antigo = self.centro2[1]
        if self.indo_para_cima2:
            self.centro2[1] -= self.velocidade2

        if self.indo_para_baixo2:
            self.centro2[1] += self.velocidade2

        if self.indo_para_direita2:
            self.centro2[0] += self.velocidade2

        if self.indo_para_esquerda2:
            self.centro2[0] -= self.velocidade2

        self.rect.centerx = self.centro2[0]
        self.rect.centery = self.centro2[1]

        colidiu = pygame.sprite.collide_mask(self, self.mapa)
        if colidiu:
            self.centro2[0] = x_antigo
            self.centro2[1] = y_antigo
            self.rect.centerx = self.centro2[0]
            self.rect.centery = self.centro2[1]