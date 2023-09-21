import pygame

pygame.mixer.init()
pygame.mixer.music.load('ddds/ex0021.mp3')
pygame.mixer.music.play(loops=1)
input()
pygame.event.wait()

"""
NAO FUNCIONA N SEI PORQUE
SE UM DIA EU VOLTAR ARRUMAR ESSE CODIGO
AUDIO ESTA EM adds/
"""