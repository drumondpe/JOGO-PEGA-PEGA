# -*- coding: utf-8 -*-
"""

@author: Pedro Drumond
"""
import pygame

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

    #textos que aparecem na tela de início
    titulo_do_jogo = fonte_texto_inicial.render(CONFIGURACOES.titulo_jogo, True, CORES.titulo)
    botao_de_inicio1 = fonte_texto_inicial.render('Pressione Barra de Espaço', True, (255, 40, 255))
    botao_de_inicio2 = fonte_texto_inicial.render('para começar', True, (255, 40, 255))
    nome_dos_criadores1 = fonte_texto_nomes.render('Keiya Nishio', True, CORES.nomes)
    nome_dos_criadores2 = fonte_texto_nomes.render('Pedro Drumond', True, CORES.nomes)

    #posicionamento na tela de início
    TELA.fill(CORES.fundo)
    TELA.blit(titulo_do_jogo, (CONFIGURACOES.largura_tela//2 - titulo_do_jogo.get_width() // 2, 90))
    TELA.blit(botao_de_inicio1, (CONFIGURACOES.largura_tela//2 - botao_de_inicio1.get_width() // 2, 270))
    TELA.blit(botao_de_inicio2, (CONFIGURACOES.largura_tela//2 - botao_de_inicio2.get_width() // 2, 310))
    TELA.blit(nome_dos_criadores1, (CONFIGURACOES.largura_tela//2 - nome_dos_criadores1.get_width() // 2, 490))
    TELA.blit(nome_dos_criadores2, (CONFIGURACOES.largura_tela//2 - nome_dos_criadores2.get_width() // 2, 520))

def apresenta_segunda_tela():
    # apresenta os textos da segunda tela
    fonte_textos = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_menor)
    player_pegador = fonte_textos.render('PLAYER PEGADOR: ', True, CORES.vermelho)
    TELA.blit(player_pegador, (CONFIGURACOES.largura_tela_fundo//2 - player_pegador.get_width() - 88, 7))
    
#def contagem_30_segundos():

#def apresenta_contagem_tempo():
    # apresenta o tempo que falta para o pegador
    #fonte_textos = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_menor)
    #imprime_contagem = fonte_textos.render('TEMPO RESTANTE: ', True, CORES.amarelo)
    #TELA.blit(imprime_contagem, (CONFIGURACOES.largura_tela_fundo//2 - imprime_contagem.get_width() + 100, 7)

def checa_eventos(TELA_INICIAL, GAME_OVER, RODANDO):
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
                if event.key == pygame.K_SPACE:
                    TELA_INICIAL = False
                    break
        
        # se estiver em jogo, verificar as seguintes
        elif not GAME_OVER:
            
            #fonte_texto_pontuacao = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_menor)
            #pontuacao_jogo = fonte_texto_pontuacao.render('Sua pontuação: {}'.format('pontuacao_player'), True, (150, 150, 150))
            #TELA.blit(MAPA)
            #TELA.blit(pontuacao_jogo, ((CONFIG.largura_tela//2 - pontuacao_jogo.get_width() // 2, 90)))

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


    return TELA_INICIAL, RODANDO
            