# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:14:15 2020

@author: Pedro Drumond
"""

import pygame

CONFIGURACOES = None
CORES = None
TEXTOS = None
TELA = None
PLAYER = None

def init(config, tela, player):
    'inicializa as variáveis das funções'

    global CONFIGURACOES, CORES, TEXTOS, TELA, PLAYER

    CONFIGURACOES = config    
    TELA = tela    
    PLAYER = player

    TEXTOS = CONFIGURACOES.textos
    CORES = CONFIGURACOES.cores

def apresenta_tela_inicial():
    'apresenta a tela de início'

    #config de fontes
    fonte_texto_inicial = pygama.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande) 
    fonte_texto_nomes = pygama.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_pequeno)

    #textos que aparecem na tela de início
	titulo_do_jogo = fonte_texto_inicial.render(CONFIGURACOES.titulo, True, CORES.titulo)
	botao_de_inicio1 = fonte_texto_inicial.render('Pressione Barra de Espaço', True, (255, 40, 255))
	botao_de_inicio2 = fonte_texto_inicial.render('para começar', True, (255, 40, 255))
	nome_dos_criadores1 = fonte_texto_nomes.render('Keiya Nishio', True, CORES.nomes)
	nome_dos_criadores2 = fonte_texto_nomes.render('Pedro Drumond', True, CORES.nomes)

    #posicionamento na tela de início
	TELA.fill(CORES.fundo)
	TELA.blit(titulo_do_jogo, (CONFIGURACOES.largura_tela//2 - titulo_do_jogo.get_width() // 2, 90))
	TELA.blit(botao_de_inicio1, (CONFIG.largura_tela//2 - botao_de_inicio1.get_width() // 2, 270))
	TELA.blit(botao_de_inicio2, (CONFIG.largura_tela//2 - botao_de_inicio2.get_width() // 2, 310))
	TELA.blit(nome_dos_criadores1, (CONFIG.largura_tela//2 - nome_dos_criadores1.get_width() // 2, 490))
	TELA.blit(nome_dos_criadores2, (CONFIG.largura_tela//2 - nome_dos_criadores2.get_width() // 2, 520))

def checa_eventos(tela_inicial, game_over, rodando):
    'avalia entradas e retorna booleanos de estado de jogo'

	# verifica inputs do usuário
	for event in pygame.event.get():
        
		# verifica, antes de tudo, se o usuário quer sair
		if event.type == pygame.QUIT:
			rodando = False
			break
        
        # se estiver na tela inicial, verificar as seguintes
		if tela_inicial:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					tela_inicial = False
					break
        
		# se estiver em jogo, verificar as seguintes
		elif not game_over:
			
			fonte_texto_pontuacao = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_menor)
			pontuacao_jogo = fonte_texto_pontuacao.render('Sua pontuação: {}'.format('pontuacao_player'), True, (150, 150, 150))
            TELA.blit(pontuacao_jogo, ((CONFIG.largura_tela//2 - pontuacao_jogo.get_width() // 2, 90)))

			if event.type == pygame.KEYDOWN:

				#if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				#	PACMAN.indo_para_baixo = True

				#elif event.key == pygame.K_UP or event.key == pygame.K_w:
				#	PACMAN.indo_para_cima = True

				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					PLAYER.indo_para_esquerda = True

				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					PLAYER.indo_para_direita = True

                elif event.key == pygame.K_SPACE:
                    PLAYER.pulando = True


			if event.type == pygame.KEYUP:

				#if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				#	PACMAN.indo_para_baixo = False

				#elif event.key == pygame.K_UP or event.key == pygame.K_w:
				#	PACMAN.indo_para_cima = False

				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					PLAYER.indo_para_esquerda = False

				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					PLAYER.indo_para_direita = False

                elif event.key == pygame.K_SPACE:
                    PLAYER.pulando = False

	return tela_inicial, rodando
            