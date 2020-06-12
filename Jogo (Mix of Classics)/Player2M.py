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

    def __init__(self, tela, config):
    #cria uma nova instância da classe Player2

        self.tela = tela
        self.config = config
        self.image = pygame.image.load('pacman.png') #mudar foto do player ou fotos
        self.rect = self.image.get_rect()
        self.screen_rect = tela.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom - 605

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