# -*- coding: utf-8 -*-
"""
Classe dos Players

Authors: Keiya Nishio and Pedro Drumond
"""

import pygame

class Player1(pygame.sprite.Sprite):
    'Classe que define o sprite do jogador'

    def __init__(self, tela, config):
    'cria uma nova instância da classe Player'

        self.tela = tela
        self.config = config
        self.image = pygame.image.load('imagens/pacman.png') #mudar foto do player ou fotos
        self.rect = self.image.get_rect()
        self.screen_rect = tela.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom - 20

        # propriedades customizadas de movimento
        self.velocidade = Configurações-M.velocidade 'VERIFICAR'
        self.centro = [self.rect.centerx, self.rect.centery]

        #booleanos de movimento
        self.indo_para_cima = False
        self.indo_para_baixo = False
        self.indo_para_direita = False
        self.indo_para_esquerda = False

    def update(self):
        'atualiza posição do player conforme a velocidade'

        if self.indo_para_cima:
            self.centro[1] -= self.velocidade

        if self.indo_para_baixo:
            self.centro[1] += self.velocidade

        if self.indo_para_direita:
            self.centro[0] += self.velocidade

        if self.indo_para_esquerda:
            self.centro[0] -= self.velocidade

        self.rect.centerx = self.centro[0]
        self.rect.centery = self.centro[1]
    

class Player2(pygame.sprite.Sprite):
    'Classe que define o sprite do jogador'

    def __init__(self, tela, config):
    'cria uma nova instância da classe Player'

        self.tela = tela
        self.config = config
        self.image = pygame.image.load('imagens/pacman.png') #mudar foto do player ou fotos
        self.rect = self.image.get_rect()
        self.screen_rect = tela.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom - 20

        # propriedades customizadas de movimento
        self.velocidade = Configurações-M.velocidade 'VERIFICAR'
        self.centro = [self.rect.centerx, self.rect.centery]

        #booleanos de movimento
        self.indo_para_cima = False
        self.indo_para_baixo = False
        self.indo_para_direita = False
        self.indo_para_esquerda = False

    def update(self):
        'atualiza posição do player conforme a velocidade'

        if self.indo_para_cima:
            self.centro[1] -= self.velocidade

        if self.indo_para_baixo:
            self.centro[1] += self.velocidade

        if self.indo_para_direita:
            self.centro[0] += self.velocidade

        if self.indo_para_esquerda:
            self.centro[0] -= self.velocidade

        self.rect.centerx = self.centro[0]
        self.rect.centery = self.centro[1]