# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:16:33 2020

Autores: Keiya Nishio Pedro Drumond
"""
import pygame

class Config():
    def __init__(self):

        self.titulo_jogo = 'Still Standing Man'
        self.pontuacao = 'Pontuação atual: XXX'
    #   self.pontuacao_record = 'Pontuação record: XXXX'
        self.largura_tela = 700
        self.largura_tela = 600
        self.FPS = 60

        self.velocidade = 5 #pixels
        
        self.cores = Cores()
        self.textos = Textos()

class Cores():
    def __init__(self):

        self.titulo = (200, 205, 70)
        self.fundo = (0, 0, 0)
        self.nomes = (200, 90, 210)
	#	self.pontuacao = (250, 250, 250)
	#	self.pontuacao_record = (250, 250, 250)

class Textos():
    def __init__(self):

		self.fonte = 'Futura ZBlk BT'
		self.tamanho_grande = 60
		self.tamanho_pequeno = 40
		self.tamanho_menor = 25

