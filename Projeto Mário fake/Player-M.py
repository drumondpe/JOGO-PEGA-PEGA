# -*- coding: utf-8 -*-
"""
Classe do Player

Authors: Keiya Nishio and Pedro Drumond
"""

import pygame

class Player(pygame.sprite.Sprite):
    'Classe que define o sprite do jogador'

    def __init__(self, tela, config):
    'cria uma nova instância da classe Player'

        self.tela = tela
        self.config = config
        self.image = pygame.image.load('imagens/pacman.png') #mudar foto do player
        self.rect = self.image.get_rect()
        self.screen_rect = tela.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom - 20

        # propriedades customizadas de movimento
        self.velocidade = Configurações-M.velocidade 'VERIFICAR'
        self.centro = [self.rect.centerx, self.rect.centery]

        #booleanos de movimento
        self.indo_para_direita = False
        self.indo_para_esquerda = False
        self.pulando = False

    def update(self):
        'atualiza posição do player conforme a velocidade'
    