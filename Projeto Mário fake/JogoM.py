# -*- coding: utf-8 -*-
"""

@author: Pedro Drumondd
"""

import pygame
import random

import FunçõesM as funcoes

from ConfiguraçõesM import Config
from PlayerM import Player

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
    PLAYER1 = Player(TELA, CONFIGURACOES)
    funcoes.init(CONFIG, TELA, PLAYER1)
    
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

            PLAYER1.update() # atualiza posição do player

            TELA.blit(PLAYER1.image, PLAYER.rect)

        elif GAME_OVER:
            pass

		pygame.display.flip()


rodar()

            