# -*- coding: utf-8 -*-
"""

@author: Pedro Drumond
"""
import pygame
import math
from Player1M import Player1
from Player2M import Player2
vetor = pygame.math.Vector2

CONFIGURACOES = None
CORES = None
TEXTOS = None
TELA = None
PLAYER1 = None
PLAYER2 = None

def init(config, tela, player1, player2):
    #inicializa as variáveis das funções

    global CONFIGURACOES, CORES, TEXTOS, TELA, PLAYER1, PLAYER2

    CONFIGURACOES = config    
    TELA = tela    
    PLAYER1 = player1
    PLAYER2 = player2

    TEXTOS = CONFIGURACOES.textos
    CORES = CONFIGURACOES.cores

def apresenta_tela_inicial():
    #apresenta a tela de início

    #config de fontes
    fonte_texto_inicial = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande) 
    fonte_texto_nomes = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_pequeno)
    fonte_texo_super = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_super)

    #textos que aparecem na tela de início
    titulo_do_jogo = fonte_texo_super.render(CONFIGURACOES.titulo_jogo, True, CORES.titulo)
    botao_de_inicio1 = fonte_texto_inicial.render('Pressione Barra de Espaço', True, (255, 40, 255))
    botao_de_inicio2 = fonte_texto_inicial.render('para começar!', True, (255, 40, 255))
    nome_dos_criadores1 = fonte_texto_nomes.render('Keiya Nishio', True, CORES.vermelho)
    nome_dos_criadores2 = fonte_texto_nomes.render('Pedro Drumond', True, CORES.vermelho)
    botoes_de_movimento1 = fonte_texto_nomes.render('AMARELO: W/A/S/D', True, CORES.amarelo)
    botoes_de_movimento2 = fonte_texto_nomes.render('AZUL: SETINHAS', True, CORES.azul_marinho)
    insper = fonte_texto_nomes.render('ENG - INSPER 2020.1', True, CORES.vermelho)


    #posicionamento na tela de início
    TELA.fill(CORES.fundo)
    TELA.blit(titulo_do_jogo, (CONFIGURACOES.largura_tela//2 - titulo_do_jogo.get_width() // 2, 90))
    TELA.blit(botao_de_inicio1, (CONFIGURACOES.largura_tela//2 - botao_de_inicio1.get_width() // 2, 270))
    TELA.blit(botao_de_inicio2, (CONFIGURACOES.largura_tela//2 - botao_de_inicio2.get_width() // 2, 310))
    TELA.blit(nome_dos_criadores1, (CONFIGURACOES.largura_tela//2 - nome_dos_criadores1.get_width() // 2, 560))
    TELA.blit(nome_dos_criadores2, (CONFIGURACOES.largura_tela//2 - nome_dos_criadores2.get_width() // 2, 590))
    TELA.blit(botoes_de_movimento1, (CONFIGURACOES.largura_tela//2 - botoes_de_movimento1.get_width()//2, 450))
    TELA.blit(botoes_de_movimento2, (CONFIGURACOES.largura_tela//2 - botoes_de_movimento2.get_width()//2, 490))
    TELA.blit(insper, (CONFIGURACOES.largura_tela//2 - insper.get_width()//2, 620))

def contador_tempo(t0): # apresenta e faz a contagem do tempo
    t1 = pygame.time.get_ticks()
    dif_tempo = (t1 - t0) // 1000
    return 60 - dif_tempo


def apresenta_segunda_tela(): # apresenta os textos da segunda tela
    fonte_textos = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_menor)
    player_pegador = fonte_textos.render('PLAYER PEGADOR: AZUL', True, CORES.aqua)
    tempo = contador_tempo(t0)
    tempo_restante = fonte_textos.render('TEMPO: {0}'.format(tempo), True, CORES.vermelho)  ### MUDAR AQUI
    TELA.blit(player_pegador, (CONFIGURACOES.largura_tela_fundo//2 - player_pegador.get_width() + 200, 7))
    TELA.blit(tempo_restante, (CONFIGURACOES.largura_tela_fundo//2 - player_pegador.get_width() - 45, 7))
    return tempo

def apresenta_tela_vencedor_pegador(): # apresenta os textos e imagem na tela do vencedor se for pegador
    fonte_textos_pegador = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_super)
    parabenizacao1 = fonte_textos_pegador.render('PARABéNS PLAYER 2', True, CORES.aqua)
    imagem_pacman_azul = pygame.image.load('pacman-azul.png').convert_alpha()
    imagem_pacman_azul = pygame.transform.scale(imagem_pacman_azul, (200, 200))

    TELA.blit(parabenizacao1, (CONFIGURACOES.largura_tela//2 - parabenizacao1.get_width() // 2, 50))
    TELA.blit(imagem_pacman_azul, (CONFIGURACOES.largura_tela//2 - imagem_pacman_azul.get_width()// 2, 200))

def apresenta_tela_vencedor_tempo(): # apresenta os textos e imagem na tela do vencedor se for fugitivo
    fonte_textos_fugitivo = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_super)
    parabenizacao2 = fonte_textos_fugitivo.render('PARABéNS PLAYER 1', True, CORES.amarelo)
    imagem_pacman = pygame.image.load('pacman.png').convert_alpha()
    imagem_pacman = pygame.transform.scale(imagem_pacman, (200, 200))

    TELA.blit(parabenizacao2, (CONFIGURACOES.largura_tela//2 - parabenizacao2.get_width() // 2 , 50))
    TELA.blit(imagem_pacman, (CONFIGURACOES.largura_tela//2 - imagem_pacman.get_width()// 2, 200))


def checa_eventos(TELA_INICIAL, GAME_OVER, RODANDO, SEGUNDA_TELA, PLAYERS_COLIDIRAM, TIME_IS_UP, tempo_restante):
    global t0
    #avalia entradas e retorna booleanos de estado de jogo

    # verifica inputs do usuário
    for event in pygame.event.get():
        
        # verifica, antes de tudo, se o usuário quer sair
        if event.type == pygame.QUIT:
            RODANDO = False
            break
        
        # se estiver na tela inicial, verificar as seguintes
        if TELA_INICIAL:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # muda para a segunda tela de jogo
                    pygame.mixer.music.load('slider-remix.mp3') 
                    pygame.mixer.music.play()
                    TELA_INICIAL = False
                    SEGUNDA_TELA = True
                    t0 = pygame.time.get_ticks()
        
        # se estiver em jogo, verificar as seguintes
        elif SEGUNDA_TELA:
            hits = pygame.sprite.collide_mask(PLAYER1, PLAYER2) # lista de colisão dos players

            if event.type == pygame.KEYDOWN:

                # configurando Player 1
                if event.key == pygame.K_s: 
                    PLAYER1.indo_para_baixo1 = True

                elif event.key == pygame.K_w:
                    PLAYER1.indo_para_cima1 = True

                elif event.key == pygame.K_a: #or event.key == pygame.K_LEFT:
                    PLAYER1.indo_para_esquerda1 = True

                elif event.key == pygame.K_d: #or event.key == pygame.K_RIGHT:
                    PLAYER1.indo_para_direita1 = True

                # configurando Player 2
                elif event.key == pygame.K_DOWN:
                    PLAYER2.indo_para_baixo2 = True

                elif event.key == pygame.K_UP:
                    PLAYER2.indo_para_cima2 = True

                elif event.key == pygame.K_LEFT:
                    PLAYER2.indo_para_esquerda2 = True

                elif event.key == pygame.K_RIGHT:
                    PLAYER2.indo_para_direita2 = True


            if event.type == pygame.KEYUP:

                # configurando Player 1
                if event.key == pygame.K_s: 
                    PLAYER1.indo_para_baixo1 = False

                elif event.key == pygame.K_w:
                    PLAYER1.indo_para_cima1 = False

                elif event.key == pygame.K_a: #or event.key == pygame.K_LEFT:
                    PLAYER1.indo_para_esquerda1 = False

                elif event.key == pygame.K_d: #or event.key == pygame.K_RIGHT:
                    PLAYER1.indo_para_direita1 = False

                # configurando Player 2
                elif event.key == pygame.K_DOWN:
                    PLAYER2.indo_para_baixo2 = False

                elif event.key == pygame.K_UP:
                    PLAYER2.indo_para_cima2 = False

                elif event.key == pygame.K_LEFT:
                    PLAYER2.indo_para_esquerda2 = False

                elif event.key == pygame.K_RIGHT:
                    PLAYER2.indo_para_direita2 = False
                
            if hits:
                pygame.mixer.music.load('winner-sound.mp3')
                pygame.mixer.music.play()

                PLAYERS_COLIDIRAM = True
                SEGUNDA_TELA = False


            if tempo_restante <= 0: # se for igual 0, muda para tela TIME_IS_UP 
                pygame.mixer.music.load('winner-sound.mp3')
                pygame.mixer.music.play()
                TIME_IS_UP = True
                SEGUNDA_TELA = False
                
        # elif PLAYERS_COLIDIRAM or TIME_IS_UP: # se tiver alguma dessas tela, verifica a entrada 

        #     if event.type == pygame.KEYDOWN:
        #         #if event.type

        #         if event.key == pygame.K_SPACE:
        #             PLAYERS_COLIDIRAM = False
        #             TIME_IS_UP = False
        #             #TELA_INICIAL = True

        #         elif event.key == pygame.K_BACKSPACE:
        #             PLAYERS_COLIDIRAM = False
        #             TIME_IS_UP = False
        #             RODANDO = False


    return TELA_INICIAL, GAME_OVER, RODANDO, SEGUNDA_TELA, PLAYERS_COLIDIRAM, TIME_IS_UP
            