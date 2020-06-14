# -*- coding: utf-8 -*-
"""

Autores: Keiya Nishio e Pedro Drumond
"""


### Precisamos fazer
# ajeitar a colisão entre os players 
# fazer a função da contagem regressiva
# ajeitar erros bestas



import pygame
import random
import math

import FunçõesM as funcoes

from ConfiguraçõesM import Config 
from ConfiguraçõesM import Textos
from Player1M import Player1
from Player2M import Player2
from MapaM import Mapa
vetor = pygame.math.Vector2
# puxa as configurações
CONFIGURACOES = Config()
TEXTOS = Textos()
CORES = CONFIGURACOES.cores

# roda o jogo
def rodar():

    #### INICIALIZA O JOGO ####
    pygame.init()
    pygame.mixer.init()

    TELA = pygame.display.set_mode((CONFIGURACOES.largura_tela, CONFIGURACOES.altura_tela))
    CLOCK = pygame.time.Clock()

    pygame.display.set_caption(CONFIGURACOES.titulo_jogo)



    # booleanos do programa
    RODANDO = True
    TELA_INICIAL = True
    SEGUNDA_TELA = False
    PLAYERS_COLIDIRAM = False
    TIME_IS_UP = False # quando o temporizador chega a zero
    GAME_OVER = False

    # inicializando objetos
    MAPA = Mapa(TELA, CONFIGURACOES)           
    PLAYER1 = Player1(TELA, CONFIGURACOES, MAPA)
    PLAYER2 = Player2(TELA, CONFIGURACOES, MAPA)    
    funcoes.init(CONFIGURACOES, TELA, PLAYER1, PLAYER2)

    #musica_starwars = pygame.mixer.music.load('') 
    #musica_starwars = pygame.mixer.music.load('force-theme.mp3')
    #musica_slide64 = pygame.mixer.music.load('slider-remix.mp3') 
    #sound_wasted = pygame.mixer.music.load('gta-wasted.mp3') 

    # apresenta a tela de início
    funcoes.apresenta_tela_inicial()

    ## LOOP PRINCIPAL ##
    
    #pygame.mixer.music.play()
    while RODANDO:
        CLOCK.tick(CONFIGURACOES.FPS)

        # atualiza booleanos do jogo
        TELA_INICIAL, RODANDO = funcoes.checa_eventos(TELA_INICIAL, GAME_OVER, RODANDO, SEGUNDA_TELA, PLAYERS_COLIDIRAM, TIME_IS_UP)

        # LOOP DO JOGO
        if SEGUNDA_TELA and not GAME_OVER and not TELA_INICIAL and not PLAYERS_COLIDIRAM and not TIME_IS_UP:
            TELA.fill(CORES.fundo)
            MAPA.tela_jogando(TELA)
            funcoes.apresenta_segunda_tela()
            #funcoes.apresenta_contagem_tempo()

            PLAYER1.update() # atualiza posição do player1
            PLAYER2.update() # atualiza posição do player2

            TELA.blit(PLAYER1.image, PLAYER1.rect)
            TELA.blit(PLAYER2.image, PLAYER2.rect)

        elif PLAYERS_COLIDIRAM: # se os players colidirem, imprime o vencedor
            TELA.fill(CORES.fundo)
            funcoes.apresenta_tela_vencedor_pegador()

        elif TIME_IS_UP: # se o tempo acabar, imprime o vencedor 
            TELA.fill(CORES.fundo)
            funcoes.apresenta_tela_vencedor_tempo()
        
        elif GAME_OVER:
            pass

        pygame.display.flip()


rodar()

            