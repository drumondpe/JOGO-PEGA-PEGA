# -*- coding: utf-8 -*-
"""

Autores: Keiya Nishio Pedro Drumond
"""

import pygame

class Config():
    def __init__(self):

        self.titulo_jogo = 'Pega-pega clássicos'
        self.pontuacao = 'Pontuação atual: XXX'
    #   self.pontuacao_record = 'Pontuação record: XXXX'
        self.largura_tela = 610
        self.altura_tela = 670
        
        self.altura_topo_tela = 50
        self.largura_tela_fundo = self.largura_tela - self.altura_topo_tela
        self.altura_tela_fundo = self.altura_tela - self.altura_topo_tela

        self.FPS = 60


        self.velocidade = 3 #pixels
        
        self.cores = Cores()
        self.textos = Textos()

class Cores(): # cores
    def __init__(self):

        self.titulo = (200, 205, 70)
        self.fundo = (0, 0, 0)
        self.nomes = (200, 90, 210)
        self.vermelho = (255, 0, 0)
        self.preto = (0, 0, 0)
        self.branco = (255, 255, 255)
        self.aqua = (0, 128, 128)
        self.azul_marinho = (0, 0, 128)
        self.verde = (0, 255, 0)
        self.laranja = (255, 165, 0)
        self.amarelo = (255, 255, 0)


class Textos(): # tamanho e fonte dos textos
    def __init__(self):

        self.fonte = 'Futura ZBlk BT'
        self.tamanho_grande = 60
        self.tamanho_pequeno = 40
        self.tamanho_menor = 25
        self.tamanho_segunda_tela = 10

