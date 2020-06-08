# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:58:07 2020

@author: Pedro Drumondd
"""

import pygame
import random

import Funções-M as funcoes

from Configurações-M import Config
from Player-M import Player

# puxa as configurações
CONFIGURACOES = Config()
TEXTOS = CONFIGURACOES.textos
CORES = CONFIGURACOES.cores

# roda o jogo
def rodar():

    #### INICIALIZA O JOGO ####

    pygame.init()
    pygame.mixer.init()

	TELA = pygame.display.set_mode((CONFIGURACOES.largura_tela, CONFIGURACOES.altura_tela))
	CLOCK = pygame.time.Clock()

	pygame.display.set_caption(CONFIG.titulo)

    # inicialização de imagens  ------>  ainda precisamos ajeitar o mapa
	MAPA = pygame.image.load('imagens/mapa.png').convert_alpha() #mudar mapa de fundo

    # booleanos do programa
	RODANDO = True
	TELA_INICIAL = True
	GAME_OVER = False

    # inicializando objetos
    PLAYER = Player(TELA, CONFIGURACOES)
    funcoes.init(CONFIG, TELA, PLAYER)
    
    # apresenta a tela de início
    funcoes.apresenta_tela_inicial()

    ## LOOP PRINCIPAL ##
    while RODANDO:
		CLOCK.tick(CONFIGURACOES.FPS)

        # atualiza booleanos do jogo
        TELA_INICIAL, RODANDO = funcoes.checa_eventos(TELA_INICIAL, GAME_OVER, RODANDO)

        # LOOP DO JOGO
        if not GAME_OVER and not TELA_INICIAL:

            TELA.fill(CORES.fundo)
            TELA.blit(MAPA, (0, 0))

            PLAYER.update() # atualiza posição do player

            TELA.blit(PLAYER.image, PLAYER.rect)

        elif GAME_OVER:
            pass

		pygame.display.flip()


rodar()

            