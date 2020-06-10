# -*- coding: utf-8 -*-
"""
Classe dos Players

Authors: Keiya Nishio and Pedro Drumond
"""

import pygame

class Player1(pygame.sprite.Sprite):
    #Classe que define o sprite do jogador

    def __init__(self, tela, config):
        #cria uma nova instância da classe Player1

        self.tela = tela
        self.config = config
        self.image = pygame.image.load('imagens/pacman.png') #mudar foto do player ou fotos
        self.rect = self.image.get_rect()
        self.screen_rect = tela.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom - 20

        # propriedades customizadas de movimento
        self.velocidade1 = ConfiguraçõesM.velocidade #VERIFICAR
        self.centro1 = [self.rect.centerx, self.rect.centery]

        #booleanos de movimento
        self.indo_para_cima1 = False
        self.indo_para_baixo1 = False
        self.indo_para_direita1 = False
        self.indo_para_esquerda1 = False

    def update(self):
        #atualiza posição do player conforme a velocidade

        if self.indo_para_cima1:
            self.centro1[1] -= self.velocidade1

        if self.indo_para_baixo1:
            self.centro1[1] += self.velocidade1

        if self.indo_para_direita1:
            self.centro1[0] += self.velocidade1

        if self.indo_para_esquerda1:
            self.centro1[0] -= self.velocidade1

        self.rect.centerx1 = self.centro1[0]
        self.rect.centery1 = self.centro1[1]
